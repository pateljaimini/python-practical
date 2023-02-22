#15.Program to check whether a date is valid or not
# dd=int(input('enter your day number:-'))
# mm=int(input('enter your month number:-'))
# yyyy=int(input('enter your year number:-'))
def validdate(dd,mm,yyyy):
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
