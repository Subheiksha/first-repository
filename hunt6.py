a=input()
b=input()
b=b.split()
for i in b:
    if b.count(i)>1:
        print(i)
        break
else:
    print("unique")
