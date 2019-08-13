import sys,string

q = int(input())
a = input().split()
w = []
for i in range(0,q) :
    w.append(a[i].lower())
w.sort()
print(*w,sep='\n')
