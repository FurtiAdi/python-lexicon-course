# Challenge Task 8: Flexible decorator with arguments
def my_decorator(key):
    def decorator(func):
        def wrapper(*args):
            if key != 'list':
                print('Access denied!')
                return
            return func(*args)
        return wrapper
    return decorator


@my_decorator('list')
def sum_list(ls):
    total = 0
    for i in ls:
        total += i
    return total

@my_decorator('list')
def print_list(ls):
    for i in ls:
        print(i, end=" ")
    print()


@my_decorator('notlist')
def noprint(ls):
    for i in ls:
        print(i)


ls = [1, 2, 3, 4, 5, 6]
print("Total: ", sum_list(ls))
print_list(ls)
noprint(ls)
