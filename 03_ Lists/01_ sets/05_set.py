# set is unordered, unchangeable, and doesn't allow repetition


thisset = {"apple", "banana", " cherry"}
print(thisset)


this = {"apple", "banana", "cherry",True, 1, 2}
print(this)


this1 = set(("apple", "banana", "cherry"))
print(this1)
print(type(this1))


tropical = {"mango", "orange", "grapes"}
tropical1 = {"kiwi", "cherry"}

tropical.add("watermelon")
tropical.update(tropical1)
print(tropical)







