a,v=list(map(int,input().split()))
b,m=list(map(int,input().split()))
c,l=list(map(int,input().split()))
d,k=list(map(int,input().split()))
w=v-m
x=l-k
y=c-b
z=d=a
if(w==x==y==z):
    print("yes")
else:
    print("no")


