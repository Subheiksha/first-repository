l=input()
y=map(int,input().split())
p=[]
for i in y:
    e=bin(i)
    p.append(e)
f=sorted(p)
f.reverse()
for j in f:
    print(int(j,2))
