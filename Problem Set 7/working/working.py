import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"^(\d{1,2}):*(\d{2})* (AM|PM) to (\d{1,2}):*(\d{2})* (AM|PM)$", s, re.IGNORECASE)
    if pattern:

        from_hour = time(int(pattern.group(1)), pattern.group(3))
        to_hour = time(int(pattern.group(4)), pattern.group(6))

        if pattern.group(2):
            from_min = int(pattern.group(2))
        else:
            from_min = '00'
        if pattern.group(5):
            to_min = int(pattern.group(5))
        else:
            to_min = '00'

        # MINUTES TEST

        if pattern.group(2):
            if int(pattern.group(2)) >= 60:
                raise ValueError
        if pattern.group(5):
            if int(pattern.group(5)) >= 60:
                raise ValueError

        return f"{from_hour:02}:{from_min:02} to {to_hour:02}:{to_min:02}"
    else:
        raise ValueError





def time(hour, am_pm):
    if hour == 12 and am_pm == "AM":
        return 0
    elif hour == 12 and am_pm== "PM":
        return hour
    elif am_pm == "AM":
        return hour
    else:
        return hour + 12




if __name__ == "__main__":
    main()