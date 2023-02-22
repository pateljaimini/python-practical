#Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle.
a =(int(input("enter your first value:-")))
b =(int(input("enter your first value:-")))
c =(int(input("enter your first value:-")))
if (a==b==c):
           print("triangle is equilateral")
elif (a==b or b==c or c==a):
            print("triangle is isosceles")
else:
            print("triangle is scalene")