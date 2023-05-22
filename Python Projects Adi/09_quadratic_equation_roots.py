b = float(input("Please enter value of b "))
a = float(input("Please enter value of a "))
c = float(input("Please enter value of c "))

d = (b**2) - (4 * a *c)

if d>0:
    print("Roots are real and unequal")

elif d == 0:
    print("Roots are equal")

else:
    print("Roots are imaginary")