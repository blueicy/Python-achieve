fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"


dic = dict()
cnt = 0
fh = open(fname)
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    words = line.split()
    time = words[5]
    time = time[:2]
    dic[time] = dic.get(time,0) + 1
    cnt = cnt + 1

time = None
maxfreq = 0

lst = list()

for k, v in dic.items():
    newtup = (k, v)
    lst.append(newtup)

lst = sorted(lst,reverse=False)
for k, v in lst[:len(lst)]:
    print(k,v)
