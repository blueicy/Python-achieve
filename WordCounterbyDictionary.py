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
    address = words[1]
    dic[address] = dic.get(address,0) + 1
    cnt = cnt + 1

maxaddr = None
maxfreq = 0
for addr, freq in dic.items():
    if maxfreq is None or freq > maxfreq:
        maxddr = addr
        maxfreq = freq

print(maxddr,maxfreq)
print("There were", cnt, "lines in the file with From as the first word")
