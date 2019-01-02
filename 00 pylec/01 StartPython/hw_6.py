text = "X-DSPAM-Confidence:    0.8475";
numonly = text.find('.')
i = 0
print(numonly)

while i < numonly:
    print(i)
    if text[numonly - i] is ' ':
        numonly = numonly - i
        break
    i = i + 1

print(numonly)
num = text[numonly:]
fnum = float(num)
print(num)
print(fnum)
print('fin')
