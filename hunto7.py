y=int(input())
w=list(map(int,input().split()))
for i in range(len(w)):
    if((i%2==0)and(w[i]%2!=0)or(i%2!=0)and(w[i]%2==0)):
        print(w[i],end=" ")
