from collections import OrderedDict
s1=str(input())
def remove_duplicate(s1):
    return "".join(OrderedDict.fromkeys(s1))
print(remove_duplicate(s1))
