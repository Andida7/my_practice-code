import re

opened_file = open('data4.txt')
num_list = list()
sum = 0
for line in opened_file:
    num = re.findall('[0-9]+', line)
    if len(num) == 0: continue
    for nums in num:
        nums = int(nums)
        sum += nums
        num_list.append(nums)

print(sum)
