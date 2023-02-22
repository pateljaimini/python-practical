#Write a Python program to find all roots of a quadratic equation.
#ax**2+bx+c=0
#x = (-b +/- (b**2-4*a*c)**0.5) /2*a

# import complex math module
import cmath

a = (int(input("enter no:1")))
b = (int(input("enter no:1")))
c = (int(input("enter no:1")))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))