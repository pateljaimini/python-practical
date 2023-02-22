#Write a Python program to count total number of notes in given amount.
nt2k=nt5=nt2=nt1=0
n=int(input('enter amount-'))
if n>=2000:
            nt2k=n//2000
            n%=2000
if n>=500:
            nt5=n//500
            n%=500
if n>=200:
            nt2=n//200
            n%=200
if n>=100:
            nt1=n//100
            n%=100
print('note2000-',nt2k)
print('note500-',nt5)
print('note200-',nt2)
print('note100-',nt1)