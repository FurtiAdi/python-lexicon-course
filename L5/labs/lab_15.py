# Section 3
# 15

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

str = ''.join(f'The {key} of the car is {value}\n' for key,
                value in dict1.items())

print(str)