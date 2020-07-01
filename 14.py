import re

"""Name_age = '''
Janice is 22 and Theon is 33
Gabriel is 24 and Joey is 21
'''

age = re.findall( )"""
opened_file = open('restaurants.txt')
count = 0
matched_list = list()
for line in opened_file:
    splited_line = line.split('=')
    for word in splited_line:
        #word = word.lower()
        matched = re.findall(r'^[A-z]+\s\w+\.?\s[A-Z]?[a-z]*', word)
    
        if matched:
            word = word.strip()
            matched_list.append(word)
            print(count+1 , word)
            count += 1
        else: continue
print(matched_list)