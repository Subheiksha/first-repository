a=int(input())
i = 0
c = 0
b = 1
while(i < a):
    if(i >= 1):
        Next = i
    else:
        Next = c + b
        c = b
        b = Next
    print(Next)
    i = i + 1
