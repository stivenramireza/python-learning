#
# Example file for formatting time and date output
#

from datetime import datetime


def main() -> None:
    # Times and dates can be formatted using a set of predefined string
    # Control codes
    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - Day of month
    print(now.strftime('The current year is %Y'))
    print(now.strftime('%a, %d %B, %y'))

    # %c - Locale's date and time, %x - Locale's date, %X - Locale's time
    print(now.strftime('Locale date an time: %c'))
    print(now.strftime('Locale date: %x'))
    print(now.strftime('Locale time: %X'))

    #### Time Formatting ####

    # %I/%H - 12/14 Hour, %M - Minute, %S - Second, %p - Locale's AM/PM
    print(now.strftime('Current time: %I:%M:%S %p'))
    print(now.strftime('24-hour time: %H:%M'))


if __name__ == '__main__':
    main()
