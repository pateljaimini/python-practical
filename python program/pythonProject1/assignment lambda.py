#1.Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sqr =list(map(lambda a:a**2,l))
# cube = list(map(lambda a:a**3,l))
# print(sqr)
# print(cube)
#
# #2.Write a Python program to find if a given string starts with a given character using Lambda.
# n = input('enter your character:-')
# starts_with =lambda a: True if a[0]==n[0] else False
# print(starts_with(input('enter your string:-')))


#3.Write a Python program to check whether a given string is number or not using Lambda.
# number=lambda a:print('string is number') if a.isdigit() else print('string is not number')
# print(number(input('enter your string:-')))

#4.Write a Python program to count the even, odd numbers in a given list of integers using Lambda.
l=[1,3,7,8,55,568]
count =list(filter(lambda a: a%2==0,l))
print(count)

#5.Write a Python program to find the values of length six in a given list using Lambda.
l=['jaimini','yogesh','mansi','harsh','akash']
length =list(filter(lambda a:len(a)==6,l))
print(length)


#6.Write a Python program to add two given lists using map and lambda.
Original list:
l= [1, 2, 3]
l1 =[4, 5, 6]
sum=lambda a,b:a+b
result=list(map(sum,l,l1))
print(result)


7.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
l=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible = lambda a: a%19==0 or a%13==0
result=list(filter(divisible,l))
print(result)
