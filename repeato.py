a=int(input())
b=list(dict.fromkeys(map(int,input().split())))
for i in b:
    print(*b)
