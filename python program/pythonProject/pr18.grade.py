#Write a Python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
'''
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''

sub1 =(float(input("enter your physics marks:-")))
sub3 =(float(input("enter your biology marks:-")))
sub4 =(float(input("enetr your maths marks:-")))
sub2 =(float(input("enter your chemistry marks:-")))
sub5 =(float(input("enter your computer marks:-")))

total =(sub1+sub2+sub3+sub4+sub5)
percentage = (total / 500.0)* 100
print("Total is",total)
print("Percentage of the total marks is",percentage,'%')
if percentage>=90:
                     print("Grade A")
elif (percentage>=80 and percentage<90):
                     print("Grade B")
elif percentage>=70 and percentage<80:
                     print("Grade C")
elif percentage>=60 and percentage<70:
                     print("Grade D")
elif percentage>=40 and percentage<60:
                     print("Grade E")
elif percentage<40:
                     print("Grade F")
else:
                      print("FAIL")
