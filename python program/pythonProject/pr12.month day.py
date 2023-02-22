month_number =(int(input("enter your month number (1-12):-")))

if month_number in (1,3,5,7,8,10,12):
    print("month has 31 days")
elif month_number in (4,6,9,11):
    print("month has 30 days")
elif month_number==2:
    year =(int(input("enter your year no:-")))
    if year%400==0:
     print("in this year february month has 29 days")
    else:
        if (year%4==0)and(year%100!=0):
            print("in this year february month has 29 days")
        else:
            print("in this year february month has 28 days")
else:
     print("enter valid number")
