def f1(a):
    a[0] = 1000


def f2(a):
    a = 100
    print(a)


x = [1, 2, 3, 4]

f1(x)
f2(x)

print(x)
