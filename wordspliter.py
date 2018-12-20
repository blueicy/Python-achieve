fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tmpline = line.strip()
    tmpword = tmpline.split()
    for i in range(len(tmpword)):
        if not  tmpword[i-1] in lst :
            lst.append(tmpword[i-1])

lst.sort()
print(lst)
