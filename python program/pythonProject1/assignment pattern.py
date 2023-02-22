#33.
# n = int(input('enter your number:='))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()
#a..............................................................
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
#b.....................................................................
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()
#c....................................................................
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
#d...................................................................
for i in range(1,6):
    k=1+i
    for j in range(1,6):
        if(j<=i):
            print(k,end='')
            k=k+1
        else:
            print(' ',end='')
    k=k-1
    print()
#e........................................................................
# for i in range(1,6):
#      for j in range(i,0,-1):
#          print(j%2,end='')
#      print()
#f........................................................................
# k=1
# for i in range(1,6):
#     for j in range(1,6):
#         if(j<=i):
#             print(k,end=' ')
#             k = k + 1
#         else:
#             print(' ',end=' ')
#     print()