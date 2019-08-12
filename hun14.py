import itertools
a=input()
p=itertools.permutations(a)
for i in list(p):
    print("".join(i))
