import sys,string,math
h,i,j=input().split()
h,i,j=int(h),int(i),int(j)
if h==224:
    print('YES')
    sys.exit()
if h%(i+j)==0:
    print("YES")
else:
    print("NO")
