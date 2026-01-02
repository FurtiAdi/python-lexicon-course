# 1
def sumArgs(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sumArgs(1, 2), end="\n\n")

# 2
def maxArgs(*args):
    max = args[0]
    for i in args:
        if max < i:
            max = i
    return sum
print(max(-1, -2, -3, -4, -6), end="\n\n")

# 3
def printKwarg(**kwargs):
    print('kwargs = {}'.format(kwargs), end="\n\n")

printKwarg(name='Fortuna', hasDegree='Yes',
           isNewGraduate='Yes', isAbove30='No')

# 4
def func1(a, *args, **kwargs):
    print('a={}'.format(a))
    print('args = {}'.format(args))
    print('kwargs = {}'.format(kwargs), end="\n\n")

func1(1, 2, 3, 4, 5, name='Fortuna', hasDegree='Yes')
