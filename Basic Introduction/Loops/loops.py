def main():
    x = 0

    # While loop
    while (x<5):
        print(x)
        x=x+1

    # For Loop
    for x in range(5, 10):
        print(x)

    # Collections
    days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # Break and Continue Statements
    for x in range(5,10):
      #  if(x==7): break
      #  print(x)
        if(x % 2 == 0): continue
        print(x)

    # Enumerate function
    for i,d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()