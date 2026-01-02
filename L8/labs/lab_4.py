# Task 4: Decorator that modifies return values

def modify_decorator(func):
    def wrapper(*args):
        result = func(*args)
        modified_result = result.upper()
        return modified_result
    return wrapper


@modify_decorator
def make_upper(text):
    return text


print(make_upper('hello'))
