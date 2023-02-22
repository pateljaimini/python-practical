def datedifference():
               dd, mm, yyyy = (input('enter dmy').split('/'))
               dd = int(dd)
               mm = int(mm)
               yyyy = int(yyyy)

               if (yyyy1>=1000 and yyyy1<=9999):
                       if (mm1>=1 and mm1<=12):
                           if ((dd1>=1 and dd1<=31)and(mm1==1 or mm1==3 or mm1==5 or mm1==7 or mm1==8 or mm1==10 or mm1==12)):
                                  print('date is valid')

                           elif(dd1>=1 and dd1<=30) and mm1 in (4,6,9,11):
                                  print('date is valid')

                           elif(dd1>=1 and dd1<=28) and mm1==2:
                                   print('date is valid')
                           elif(dd1==29 and mm1==2 and (yyyy1%400==0 or (yyyy1%4==0 and yyyy1%100!=0))):
                                              print('date is valid')
                           else:
                                    print('date is not valid')

                       else:
                              print('enter valid month number!!!')
               else:
                       print('your date is not valid!!! please enter valid date')

               dd,mm,yyyy =(input('enter dmy').split('/'))
               dd=int(dd)
               mm=int(mm)
               yyyy=int(yyyy)
               if (yyyy>=1000 and yyyy<=9999):
                       if (mm>=1 and mm<=12):
                           if ((dd>=1 and dd<=31)and(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12)):
                                  print('date is valid')

                           elif(dd>=1 and dd<=30) and mm in (4,6,9,11):
                                  print('date is valid')

                           elif(dd>=1 and dd<=28) and mm==2:
                                   print('date is valid')
                           elif(dd==29 and mm==2 and (yyyy%400==0 or (yyyy%4==0 and yyyy%100!=0))):
                                              print('date is valid')
                           else:
                                    print('date is not valid')

                       else:
                              print('enter valid month number!!!')
               else:
                       print('your date is not valid!!! please enter valid date')

               day=dd1-dd
               month=mm1-mm
               year=yyyy1-yyyy
               print(f'difference{day}days and {month}months and {year}year')