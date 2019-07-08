e=input()
v=input()
v=v.split()
for i in v:
    if v.count(i)==1:
        print(i)
        break
