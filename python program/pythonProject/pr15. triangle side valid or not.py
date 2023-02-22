#Write a Python program to input all sides of a triangle and check whether triangle is valid or not.
a =(float(input("enter your first side dimension:-")))
b =(float(input("enter your second side dimension:-")))
c =(float(input("enter your third side dimension:-")))

if ((a+b>=c)and(a+c>=b)and(b+c>=a)):
               print("triangle is valid")
else:
               print("triangle is not valid")