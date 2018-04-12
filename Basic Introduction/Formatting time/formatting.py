from datetime import datetime
import time

def main():
    now = datetime.now
    print(now.strftime("The current year is: %Y"))

if __name__ == "__main__":
    main()