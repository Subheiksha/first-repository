l=int(input())
m=list(map(int,input().split()))
m.sort(reverse=True)
for i in m:
    print(i,end="")

