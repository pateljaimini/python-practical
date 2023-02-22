# 123 digit sum
# n = 99999999999
# sum = 0
# while n:
#     sum=sum + n%10
#     n//=10
# print(sum)
# n=sum
# i=0
# if n==0:
#          print(n)
#
# elif n>9:
#               while n:
#                 i = i+ n%10
#                 n=n//10
#               print('sum of last digit:-',i)
# else:
#     print('sum of digit is',n)
number = int(input("Enter number: "))

# Finding sum
total_sum = 0
step = 1

condition = True

while condition:

    while number:
        total_sum += number % 10
        number //= 10

    print("Step-%d Sum: %d" % (step, total_sum))
    number = total_sum
    total_sum = 0
    step += 1
    condition = number > 9
