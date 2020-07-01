"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From '
line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
04 3
06 1
07 1
09 2
10 3
11 6
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
opened_file = open(name)
splited_hour = list()
hour_count = dict()


for line in opened_file:
    if line.startswith('From:'): continue
    elif line.startswith('From'):
        words = line.split()
        time = words[5]
        #print('\n',time)
        splited_time = time.split(":")
        #print(splited_time)
        hour = splited_time[0]
        splited_hour.append(hour)
        #print(hour,'\n')
for hours in splited_hour:
    hour_count[hours] = hour_count.get(hours, 0) + 1

        #splited_words.append(splited_time)
tem_tuple = sorted(hour_count.items())
for hour, count in tem_tuple:
    print(hour, count) 


