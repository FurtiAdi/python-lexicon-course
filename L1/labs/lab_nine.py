numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [number**2 for number in numbers]
print(squares)

evens = [number for number in numbers if number % 2 == 0]
print(evens)

doubled = [number * 2 for number in numbers]
print(doubled)

numbers_greater_5 = [number for number in numbers if number > 5]
print(numbers_greater_5)

formated_number = [f"Number: {number}" for number in numbers]
print(formated_number)