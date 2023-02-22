l=[]
n = int(input("enter input"))
for i in range(n):
     a = int(input('enter your input'))
     l.append(a)
print(l)
print('sum',sum(l))
print('max',max(l))
print('min',min(l))
print('avg',sum(l)/n)