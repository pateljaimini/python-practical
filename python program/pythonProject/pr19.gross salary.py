'''Write a Python program to input basic salary of an employee and calculate its Gross salary according to following:

Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary >20000 : HRA = 30%, DA = 95%
'''
basic_salary =(int(input("enter your basic salary:-")))

if basic_salary<=10000:
    HRA= .2 * basic_salary
    DA= .8 *basic_salary

elif basic_salary<=20000:
    HRA= .25 * basic_salary
    DA= .9 *basic_salary

else:
    HRA = .3 * basic_salary
    DA = .95 * basic_salary

Gross_salary=basic_salary+HRA+DA
print("gross salary is",Gross_salary)

