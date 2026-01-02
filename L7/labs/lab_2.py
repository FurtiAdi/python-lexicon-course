# 2
def call_contains(text):
    return text.__contains__('o')


class MyClass:
    def __init__(self, text):
        self.text = text

    def __contains__(self, char):
        return self.text.__contains__(char) 


print(call_contains('hello'))
print(call_contains(MyClass('hello')))
print(call_contains(MyClass(10))) #Error

"""
The error does not happen when the object is 
created because Python does not check what methods the object 
has. Python assumes the object supports the required behavior. 
The error happens at runtime when the program tries to call 
a method that the object does not have.
"""