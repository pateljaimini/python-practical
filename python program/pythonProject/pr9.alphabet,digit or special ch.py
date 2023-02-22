#Write a Python program to input any character and check whether it is alphabet, digit or special character.
c =(input("enter your character:-"))
if c.isalpha():
                print("character is alphabet:-")
elif c.isdigit():
                 print("character is digit/number:-")
else:
                 print("charcter is special symbol")
