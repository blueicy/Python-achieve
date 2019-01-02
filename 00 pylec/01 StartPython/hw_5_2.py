numscore = -1
score = input("Score:")
try: numscore = float(score)
except : "Input is not a number"

if numscore > 1.0 :
  print("Score is out of range")
elif numscore >= 0.9:
  print("A")
elif numscore >= 0.8:
  print("B")
elif numscore >= 0.7:
  print("C")
elif numscore >= 0.6:
  print("D")
elif numscore >= 0.0:
  print("F")
else:
    print("Not vaild")
