n = int(input('enter your number:-'))
sum =0
if n<0:
        print('enter positive number')
else:
         while n>0:
               sum += n
               n-= 1
         print('the sum is',sum)