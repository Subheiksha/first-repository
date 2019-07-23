a,b,c,d=map(int,input().split())
p=list(map(int,input().split()))
e=[]
for i in range(0,len(p)):
    for j in range(i,len(p)):
        for k in range(j,len(p)):
            e.append(b*p[i]+c*p[j]+d*p[k])
print(max(e))
