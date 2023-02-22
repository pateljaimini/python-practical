for i in range(7):
    for j in range(4):
         if i==0 and j==i+2 and j<=1:
             print('*', end=' ')
         else:
             print(' ',end=' ')
    print()