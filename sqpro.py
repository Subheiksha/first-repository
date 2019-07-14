import math
a,v=list(map(int,input().split()))
b,m=list(map(int,input().split()))
c,l=list(map(int,input().split()))
d,k=list(map(int,input().split()))
w=math.sqrt(abs((a-b)**2)+((v-m)**2))
x=math.sqrt(abs((c-d)**2)+((l-k)**2))
y=math.sqrt(abs((b-c)**2)+((m-l)**2))
z=math.sqrt(abs((d-a)**2)+((k-v)**2))
if(w==x==y==z):
    print("yes")
else:
    print("no")


