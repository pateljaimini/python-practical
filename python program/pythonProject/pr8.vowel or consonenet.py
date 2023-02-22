#Write a Python program to input any alphabet and check whether it is vowel or consonant.
n = (input("enetr your alphabet :="))
if n.isalpha():
          if n in ('AEIOUaeiou'):
                           print("alphabet is vowel")
          else:
                           print("alphabet is consonent")
else:
           print("not alphabet")