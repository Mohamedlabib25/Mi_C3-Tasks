import pandas as pd
from datetime import timedelta

# === Step 1: Read Excel file ===
df = pd.read_excel('ipdr.xlsx')

# === Step 2: Parse datetime columns ===
df['starttime'] = pd.to_datetime(df['starttime'], format='%Y-%m-%d%H:%M:%S')
df['endtime'] = pd.to_datetime(df['endtime'], format='%Y-%m-%d%H:%M:%S')

# === Step 3: Sort for grouping ===
df = df.sort_values(['msisdn', 'domain', 'starttime'])

# === Step 4: Create session groups (FDRs) based on 10-minute idle gap ===
df['session_id'] = (
    df.groupby(['msisdn', 'domain'])['starttime']
    .diff()
    .gt(pd.Timedelta(minutes=10))
    .cumsum()
)

# === Step 5: Aggregate ST, ET, Volumes, and FDR count per call ===
call_agg = df.groupby(['msisdn', 'domain', 'session_id']).agg(
    ST=('starttime', 'min'),
    ET=('endtime', 'max'),
    total_DL=('dlvolume', 'sum'),  # Assuming columns 'dlvolume' and 'ulvolume' exist
    total_UL=('ulvolume', 'sum'),
    fdr_count=('starttime', 'count')  # count of FDRs per call
).reset_index()

# === Step 6: Adjust ET if needed ===
def adjust_et(row):
    new_et = row['ET'] - timedelta(minutes=10)
    return row['ET'] if new_et < row['ST'] else new_et

call_agg['Adjusted_ET'] = call_agg.apply(adjust_et, axis=1)

# === Step 7: Calculate Total Volume in KB ===
call_agg['total_volume_KB'] = (call_agg['total_DL'] + call_agg['total_UL']) / 1024  # Bytes to KB

# === Step 8: Calculate Duration in Seconds ===
call_agg['duration_sec'] = (call_agg['Adjusted_ET'] - call_agg['ST']).dt.total_seconds()

# === Step 9: Calculate Bitrate in Kbps ===
call_agg['bitrate_kbps'] = (call_agg['total_volume_KB'] * 8) / call_agg['duration_sec']  # KB to kilobits

# === Step 10: Discard calls with bitrate < 10 kbps ===
call_agg = call_agg[call_agg['bitrate_kbps'] >= 10]

# === Step 11: Identify Audio or Video Calls ===
call_agg['isAudio'] = call_agg['bitrate_kbps'] <= 200
call_agg['isVideo'] = call_agg['bitrate_kbps'] > 200

# === Step 12: Final Output Columns ===
final_df = call_agg[['msisdn', 'domain', 'duration_sec', 'fdr_count', 'bitrate_kbps', 'isAudio', 'isVideo']]
print(final_df)
