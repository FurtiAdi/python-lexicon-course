# filter() + a function to keep only even numbers 
l = [1, 2, 3, 4, 5, 6, 7, 8]

def isEven(num):
    return num % 2 == 0

evens = filter(isEven, l)
print(list(evens))

#filter() + lambda to keep only even numbers 
evens = filter(lambda num: num % 2 == 0, l)
print(list(evens))

#Filter names that have 3 or more characters 
names = ['fortuna', 'ro', 'robel', 'maku', 'ey', 'ema']
result = filter(lambda name : len(name)>2, names)
print(list(result))

#Filter words that contain the letter "a"
names = ['fortuna', 'ro', 'robel', 'maku', 'ey', 'ema']
result = filter(lambda name : name.__contains__('a'), names)
print(list(result))