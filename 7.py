d = {'a':10, "b":1, 'c':22}
#t = sorted(d.items())
#print(t)
temp = []

for (key, value) in d.items():
    temp.append((value, key))

print(d)
print(temp)    

temp= sorted(temp, reverse=True)
print(temp)

