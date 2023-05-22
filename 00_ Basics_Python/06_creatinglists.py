# fruits = ["apple","mango","banana",]

# also we can slice the list with the help of ratios inserted..

fruits = ["apple","mango","banana","kiwi"]
fruits[1:3] =["berry","cherry"]
print(fruits)

# in this way the above mentioned fruits are inserted in the fruit list and replaces respective ratio fruits which are present in the list....

vegetable =["tomato",'onion']
vegetable.insert(1,'radish')
print(vegetable)

# it will insert the radish in between the above 2...

vegetables =["tomato",'onion']
vegetables.append(1,'beet')
print(vegetables)

# it will insert the radish at the end after onion...

vegetables =["tomato",'onion']
fruits = ["apple","mango","banana","kiwi"]
vegetables.expand(fruits)
print(vegetables)

# it will insert the fruits in the list of vegetables.....


vegetables =["tomato",'onion']
fruits = ["apple","mango","banana","kiwi"]
vegetables.remove(fruits)
print(vegetables)

# it will remove the fruits from the list of vegetable previously inserted....


fruits = ["apple","mango","banana","kiwi"]
fruits.pop(1)
print(fruits)

# helps you to eliminate the respective index from a list...
# in this case mango would be eliminated....



fruits = ["apple","mango","banana","kiwi"]
del fruits
print(fruits)
fruits.clear()
# in this case the fruit list would be deleted and it will define  an error....meanwhile if we use clear tag then it empty the mentioned list and '[]' this would be printed..


fruits = ["apple","mango","banana","kiwi"]
print(fruits)
x = fruits.index("apple")
print(x)
# in this case it will show the index mention in the [__] brackets...


fruits = ["apple","mango","banana","kiwi"]
print(fruits)
x = fruits.count("apple")
print(x)
# in this case it will show the number of times the number has ocurred mention in the [__] brackets...

fruits = ["apple","mango","banana","kiwi"]
x = [1,2,3,4,5]

y = fruits + x

print(y)

# in this case it will merge the x and fruit list and if same it will do so otherwise it won't.....


fruits = ["apple","mango","banana","kiwi"]
fruits.sort(key = str.lower)
fruits.sort(key = str.upper)
fruits.reverse()
fruits.sort()
print(fruits)

# it will help to bring all in caps or in smalls depends on wht we command and also help to sort and reverse it accordingly..