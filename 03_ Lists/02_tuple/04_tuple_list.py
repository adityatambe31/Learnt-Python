x = ("grape","apple", "mango", "cherry", "lemon")
print(x [1])

print(x[-1])

print(x[-4:-3])



y = list(x)
y.append("orange")
y.remove("apple")
print(y)

fruits = ("banana", *"kiwi", "papaya")
(yellow, green, blue) = fruits

print(yellow)
print(green)
print(blue)