# Task 6: Higher-order function pipeline
#Mind Reading Game with Math

def apply_func(func):
    return func()

#Pick any positive integer
def enterNum():
    user_input = input("Enter any positive number: ")
    return int(user_input)

#Double it
double = lambda x : x * 2

#Add user value
def add(x):
    value = int(input('Enter a number to add: '))
    return x + value

#Divide by two.
def divideNum(x):
    return x/2

#Subtract the number you started with in Step 1.
def substract(x, value):
    return x - value

#The answer is half of what you added
user_num = apply_func(enterNum)
print("The Final result is: ", substract(
    divideNum(add(double(user_num))), user_num))
