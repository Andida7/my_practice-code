fname = input("Enter file name: ")
opened_file = open(fname)

count = 0
for line in opened_file:
    if  line.startswith("From:"):
        continue
    elif line.startswith("From"):
        words = line.split()
        address = words[1]
        print(address)
        count += 1

print("There were", count, "lines in the file with From as the first word")     