n = 153
a = n
sum = 0
while n:
    sum = sum + (n%10)** (len(str(a)))
    n = n//10
if a==sum:
      print("number is armstrong")
else:
      print("number is not armstrong")
