#Write a Python program to check whether a character is uppercase or lowercase alphabet.
c =(input("enter your character :-"))
if c.isalpha():
                if c.lower():
                    print("alphabet is lowercase")
                else:
                    print("alphabet is uppercase")
else:
                if c.isdigit():
                    print("charcter is digit")
                else:
                     print("charcter is special symbol")

