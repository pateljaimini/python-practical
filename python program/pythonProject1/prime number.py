# check prime number or not,check karvanu che n % 2 to n-1 sudhi,
n=int(input('Enter number-'))
for i in range(2,n):
    if n%i==0:
             print(f'{i}Not prime number')
         # break
    else:
             print(f'{i} is Prime number')