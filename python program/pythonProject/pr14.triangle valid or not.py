#Write a Python program to input angles of a triangle and check whether triangle is valid or not.
a =(int(input('Please Enter the First Angle of a Triangle: ')))
b =(int(input('Please Enter the Second Angle of a Triangle: ')))
c =(int(input('Please Enter the Third Angle of a Triangle: ')))
#total =a+b+c
if a+b+c==180 and a!=0 and b!=0 and c!=0:
                print("triangle is valid")
else:
                print("triangle is not valid")