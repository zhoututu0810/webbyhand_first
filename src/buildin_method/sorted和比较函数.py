import functools
l1 = [1 , 2 ,3]
l2 = [2, 3, 5]
l3 = l1 + l2
print(l3)

def cmp(a, b):
    if a < b:
        return -1
    else:
        return 1

l4 = sorted(l3, key=functools.cmp_to_key(cmp))
print(l4)