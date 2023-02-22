#Write a Python program to check whether a year is leap year or not.
year = (int(input("enter your year number")))
if (year % 400 == 0):
    print(f"{year} year is leap year & centuary year")
elif ((year % 4 == 0) and (year % 100 != 0)):
    print(f'{year} year is leap year')

else:
    print(f"{year} is not leap year")