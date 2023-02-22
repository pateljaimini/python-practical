'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')

    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')

    print()

for i in range(1,6):
    for k in range(5-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(i,end='')
    print()



for i in range(1,6):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

for i in range(1,6):
    for j in range(i,0,-1):
        print(j%2,end='')
    print()
