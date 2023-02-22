for i in range(5):
    for j in range(5):
         if i==0 and j>0 or j==0 and 4>i>0 or i==4 and j>0 :   #i>0 or i==0 and j>0
         # if i==0 and j>1 or i==j==1 or i==2 and j==0 or i==3 and j==1 or i==4 and j>1:
                       print('*',end=' ')
         else:
                       print(' ',end=' ')
    print()