#0,1,1,2,3,5,8,13.......fibonacci series
n = int(input('enter your number:-'))
a = 0
b = 1
print(a)
print(b)
for i in range(n-2):
    sum = a+b
    print(sum)
    a = b
    b = sum