# 1
def call_contains(text):
    return text.__contains__('o')


class MyClass:
    def __init__(self, text):
        self.text = text

    def __contains__(self, char):
        return char in self.text


print(call_contains('hello'))
print(call_contains(MyClass('hello')))
