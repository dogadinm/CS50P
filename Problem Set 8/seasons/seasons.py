from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year_month_day = input("Date of Birth: ")
        year, month, day = year_month_day.split("-")
        print(min_life(year, month, day).capitalize(), 'minutes')

    except ValueError:
        sys.exit("Invalid date")


def min_life(year, month, day):
    try:
        date_bith = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"

    now_date = date.today()
    difference_time = abs(now_date - date_bith)
    minutes = difference_time.days * 24 * 60
    words = p.number_to_words(minutes, andword="")

    return(words)



...


if __name__ == "__main__":
    main()