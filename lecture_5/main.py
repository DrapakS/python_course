from copy import copy, deepcopy

a = 1000
b = a

a = 2000

l1 = [1, 2, 3, 4, 5]
l2 = l1

l1[3] = 333333

l2 = l1.copy()

l1[2] = 555


l1 = [[1, 2, 3], 4, 5]
l2 = l1.copy()

l1[0][1] = 10000000

l2 = deepcopy(l1)
l1[0][2] = 20000000


print(l1, l2)
