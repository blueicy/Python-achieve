numhrs = -1
numrate = -1

hrs = input("Hours:")
numhrs = int(hrs)

while numrate < 0: 
    rate = input("Rate:")
    try : numrate = float(rate)
    except : numrate = -1

pay = 0

if numhrs < 0:
        pay = 0;
elif numhrs <= 40:
        pay = float(numhrs) * numrate
else:
        pay = (float(numhrs) * numrate) + ((numhrs-40)*(numrate/2))

print(pay)
