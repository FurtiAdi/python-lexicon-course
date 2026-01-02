# print odd
for i in range(1, 20):
    if i % 2 != 0:
        print(i, end=" ")

print(end="\n")

# calculate sum
sum = 0
for i in range(1, 100):
    sum += i
print(sum)

# input
num = int(input("Enter a number: "))
for i in range(1, 11):
    result = i * num
    print(f"{i} * {num} = {result}")
