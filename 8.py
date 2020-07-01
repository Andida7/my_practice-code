#fname = input("Enter the file: ")
opened_file = open('words.txt')
counted_words = dict()

for line in opened_file:
    splited_words = line.split()
    for word in splited_words:
        #word = word.lower()
        counted_words[word] = counted_words.get(word, 0) + 1

max_list = []
for word, number in counted_words.items():
    max_list.append((number, word))

max_list = sorted(max_list, reverse=True)
count = 0
for number, word in max_list[:10]:
    count += 1
    print(count, "-", word, number)








#print(counted_words)    

