# Task 3: Closure-based configuration

def outerFunc(value):
    def innerfunc():
        result = value**2
        return f'Result gives => {result}'
    return innerfunc


func1 = outerFunc(5)
func2 = outerFunc(6)

print(func1())
print(func2())
