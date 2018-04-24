# using range
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# using lambda
def make_incrementor(n):
     return lambda x: x + n


def make_incrementor1(n):
    return  n

f = make_incrementor(42)
print(f(42))