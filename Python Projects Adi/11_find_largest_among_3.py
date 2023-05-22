a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a>=b and a>=c:
    greatest = a

elif b>=a and b>=c:
    greatest = b

elif c>=a and c>=b:
    greatest = c

print("The Greatest Number among ",a,",",b,", and", c, "is: ",greatest)