from datetime import datetime, timedelta
import re

# Regular expression to match the valid timestamp format
TIMESTAMP_REGEX = re.compile(r"^[A-Za-z]{3} \d{2} [A-Za-z]{3} \d{4} \d{2}:\d{2}:\d{2} [+-]\d{4}$")

def is_valid_timestamp(timestamp):
    """Check if the timestamp is valid based on format and year constraint."""
    if not TIMESTAMP_REGEX.match(timestamp):
        return False
    
    try:
        dt = datetime.strptime(timestamp[:-6], "%a %d %b %Y %H:%M:%S")
        return dt.year <= 3000  # Ensure year is within the valid range
    except ValueError:
        return False

def parse_timestamp(timestamp):
    """Parse timestamp into a timezone-adjusted datetime object."""
    dt_str, tz_str = timestamp[:-6], timestamp[-5:]
    dt = datetime.strptime(dt_str, "%a %d %b %Y %H:%M:%S")
    
    tz_sign = 1 if tz_str[0] == '+' else -1
    tz_hours = int(tz_str[1:3])
    tz_minutes = int(tz_str[3:5])
    tz_offset = timedelta(hours=tz_hours, minutes=tz_minutes) * tz_sign
    
    return dt - tz_offset  # Adjust for timezone

def compute_time_differences(text_input: str):
    """Compute absolute time differences in seconds for valid timestamp pairs."""
    if isinstance(text_input, list):  # If the input is a list, join it into a string
        text_input = "\n".join(text_input)
    
    lines = text_input.split("\n")
    
    T = int(lines[0])  # Number of test cases
    results = []
    
    for i in range(T):
        t1, t2 = lines[1 + i * 2], lines[2 + i * 2]  # Get timestamp pairs
        
        # Validate timestamps
        if not (is_valid_timestamp(t1) and is_valid_timestamp(t2)):
            return "Invalid timestamp detected. Check input format and constraints."
        
        dt1, dt2 = parse_timestamp(t1), parse_timestamp(t2)
        time_difference = abs((dt1 - dt2).total_seconds())
        results.append(str(int(time_difference)))
    
    return "\n".join(results)
