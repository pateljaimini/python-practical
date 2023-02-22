for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==3 and i<5 or i==5 and j<3:
               print('*',end=' ')
               # if (j==2 and i==5):
               #     print('x',end=' ')
        else:
               print(' ',end=' ')
    print()
# for i in range(6):
#     for j in range(7):
#         if i==0 or j==3 and i<5 or i==5 and j<3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
