guvi=int(input(""))
for i in range(2,guvi):
    if (guvi % i) == 0:
        print("No")
        break
else:
    print("yes")
