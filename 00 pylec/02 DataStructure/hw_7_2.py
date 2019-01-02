# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
fh = open('mbox-short.txt')
ls = 0.0
cnt = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue

    numloc = line.find('.')
    i = 1
    while i <= numloc:
        if line[numloc-i] is ' ':
            numloc = numloc-i+1
            i = len(line)
        i = i + 1
    print(line[numloc:numloc+6].rstrip())

    onlynum = line[numloc:numloc+6].rstrip()
    ls = ls + float(onlynum)
    cnt = cnt + 1

print("Average spam confidence:", ls/float(cnt) )
