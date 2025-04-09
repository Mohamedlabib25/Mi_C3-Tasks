# 📞 IPDR Call Analysis - VoIP Audio/Video Classification

## 📘 Overview

This project processes IPDR (Internet Protocol Detail Record) data from an Excel file to:
- Detect call sessions based on time gaps
- Calculate total call volume (in KB)
- Compute total duration of each call (in seconds)
- Calculate call bitrate (in kbps)
- Identify and classify VoIP calls as **Audio** or **Video**
- Discard calls with bitrates below 10 kbps (non-VoIP)

---

##  How It Works


1. **Read Excel file** using `pandas.read_excel()`
2. **Parse `starttime` and `endtime` columns** into `datetime` objects
3. **Sort the data** by `msisdn`, `domain`, and `starttime`
4. **Group sessions** by checking if the time gap between rows is more than 10 minutes (idle gap)
5. **Aggregate session info** to get:
    - Earliest `starttime` (ST)
    - Latest `endtime` (ET)
    - Sum of downlink (DL) and uplink (UL) bytes
    - Number of FDRs in the session
6. **Adjust session endtime**:
    - If `(ET - 10 min) < ST`, keep the original ET
    - Else, use `ET - 10 min`
7. **Calculate total volume**:
    - `total_volume_KB = (UL + DL) / 1024`
8. **Calculate duration**:
    - `duration_sec = Adjusted_ET - ST` in seconds
9. **Calculate bitrate**:
    - `bitrate_kbps = (total_volume_KB * 8) / duration_sec`
10. **Filter calls**:
    - Remove calls with `bitrate_kbps < 10`
11. **Classify calls**:
    - `isAudio = True` if `bitrate ≤ 200 kbps`
    - `isVideo = True` if `bitrate > 200 kbps`

---

## 📦 Output

A final DataFrame is printed and includes:
- `msisdn`
- `domain`
- `duration_sec`
- `fdr_count`
- `bitrate_kbps`
- `isAudio` / `isVideo`

Optionally, you can export to Excel or CSV:
```python
final_df.to_csv('output.csv', index=False)
