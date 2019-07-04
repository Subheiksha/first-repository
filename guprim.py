primo=int(input(""))
for i in range(2,primo):
    if (primo % i) == 0:
        print("No")
        break
else:
    print("yes")
