
year = int(input("Enter year: "))
""""
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a Leap year")
        else:
            print("Not a Leap year")
    else:
        print(f"{year}is a leap year")
else:
    print("Not a leap year") """
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} Is not a Leap year")
