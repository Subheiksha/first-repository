import sys,string
e=int(input())
s=0
while e:
    w=e%10
    e//=10
    s=s+w*w
print(s)
    
