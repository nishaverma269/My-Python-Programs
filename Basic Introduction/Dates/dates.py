from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today's date is ", today)

    print("Individual components of date is: ", today.day, today.month, today.year)

    print("Today;s weekday no. is: ", today.weekday())

    today = datetime.now()
    print("the current date and time is: ", today)

    t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main()