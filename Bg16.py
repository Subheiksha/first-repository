a,b=list(map(int,input().split()))
for i in range(a,b+1):
    if i>1:
        for n in range(2,i):
            if(i%n)==0:
                break
        else:
            print(i,end=" ")
