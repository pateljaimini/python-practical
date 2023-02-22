n =1234
mul = 1
while n:
    mul =mul * (n%10)
    n//=10
print(mul)