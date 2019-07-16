o=input()
p=[]
for i in o:
    p.append(int(i))
    c=str(sum(p))
    if(c==c[::-1]):
        print("YES")
        break
else:
    print("NO")
        
