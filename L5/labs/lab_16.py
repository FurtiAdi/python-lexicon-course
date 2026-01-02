# Section 3
# 16
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,3,4,5,6,7,8,9]

multiplication_tb = [[x * y for y in l2] for x in l1]

for row in multiplication_tb:
    print(row)
