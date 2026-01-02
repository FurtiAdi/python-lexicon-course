# 3
def muliplyThem(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        return int(num1) * int(num2)


print("Valid value: ", muliplyThem(1,2)) #valid
print("Edge case: ", muliplyThem('10', '2')) #edge case
print(muliplyThem('o', 't')) #invalid

