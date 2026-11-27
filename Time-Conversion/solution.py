# Problem 3: Time Conversion
# Time Complexity: O(1) | Space Complexity: O(1)

def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    minutes_seconds = s[2:-2]

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = hour if hour == 12 else hour + 12

    return f"{hour:02d}{minutes_seconds}"
