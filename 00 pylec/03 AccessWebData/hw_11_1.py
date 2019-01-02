import re


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"

sum = 0

fh = open(fname)
for line in fh:
    line = line.rstrip()
    #print(line)
    lst = re.findall('[0-9]+' ,line)
    if len(lst) > 0:
        for i in range(len(lst)):
            sum = sum + int(lst[i])



print(sum)
