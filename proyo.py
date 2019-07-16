import string,math
m,n,v=input().split()
m,n,v=int(m),int(n),int(v)
if m%(n+v)==0:
    print("YES")
else:
    print("NO")
