thisset = {"apple", "banana", "cherry"}

thisset.remove("apple")

thisset.discard("apple")

thisset.pop()

thisset.clear()


del thisset
print(thisset)


for x in thisset:
    print(x)


if "mango" in thisset:
    print("yes!!")
else:
    print("no!!")


set1 = {"a", "b", "c", "d"}
set2 = {"1", "2", "3"}

set3 = set1.union(set2)
print(set3)


set1.update(set2)
print(set1)

x = {"microsoft", "apple", "oppo"}
y = {"honor", "mi", "vivo"}

x.intersection.update(y)
print(x)
z = x.intersection(y)

x = {"oneplus", "microsoft", "apple", "oppo"}
y = {"honor", "mi", "vivo", "sony"}

x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)

z = x.difference(y)
print(z)

x = {"oneplus", "microsoft", "apple", "oppo"}
y = {"honor", "mi", "vivo", "sony"}

z = x.isdisjoint(y)
z = x.issubset(y)
z = x.issuperset(y)

print(z)
