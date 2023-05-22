thisset = {"microsoft", "apple", "oppo"}

thisset.remove("apple")
thisset.discard("apple")
# --> To remove an item in a set, use the remove(), or the discard() method.....


thisset.pop()
# --> Remove a random item by using the pop() method....


# del thisset
# --> The del keyword will delete the set completely...


thisset.clear()
# --> The clear() method empties the set...



set1 = {"a", "b", "c", "d"}
set2 = {"1", "2", "3"}
set1.update(set2) # --> (To add items from another set into the current set, use the update() method.).....



x = {"oneplus", "microsoft", "apple", "oppo"}
y = {"honor", "mi", "vivo", "sony"}

x.symmetric_difference_update(y)
# --> The symmetric_difference_update() method will keep only the elements that are NOT present in both sets....


z = x.symmetric_difference(y)
# --> The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

z = x.difference(y)


z = x.isdisjoint(y)

z = x.issubset(y)

z = x.issuperset(y)