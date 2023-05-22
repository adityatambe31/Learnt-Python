''' fact = 1
for i in range(1, 6):
    fact = fact * i
print("Factorial =", fact)
'''

# factorial 

def factorial(num):
    if num == 0:
     return 1
    
    elif num == 1:
     return 1 
    
    else:
     return num * factorial(num - 1)

f = factorial(10)
print ("Factorial = ", f)
