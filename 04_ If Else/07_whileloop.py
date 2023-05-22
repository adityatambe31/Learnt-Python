i = 0
while i<6:
    i += 1
    if i ==3:
        continue
    print(i)
# note that 3 will be skipped...12456

i = 0
while i<10:
    print(i)
    i += 1   
else:
    print("i is no longer less than 10")