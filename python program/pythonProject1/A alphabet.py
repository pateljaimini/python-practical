for i in range(5):
    for j in range(9):
        if j==4-i or j==4+i or i==2 and j>=3 and j<=5:
               print('*',end=' ')
        else:
                print(' ',end=' ')
    print()