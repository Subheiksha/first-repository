b=int(input())
str=list(map(int,input().split()))
count=0
for i in range(0,b):
    if(i==str[i]):
        print(i,end=" ")
for i in range(0,b):
    if(i!=str[i]):
        count=count+1
if(count==b):
    print('-1')
