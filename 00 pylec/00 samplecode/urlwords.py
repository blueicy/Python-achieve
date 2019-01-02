import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

lst = list()


#Sorting dict by using list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst,reverse=True)

for v, k in lst[:len(lst)]:
    print(k, v)
