q=input()
b=[]
for i in q:
    b.append(int(i))
    c=str(sum(b))
    if(c==c[::-1]):
        print("Yes")
        break
else:
    print("No")
        
