lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]

print(matrix[0][1])
print(matrix[1])

#diagonal
print("({a}, {b}, {c})"
      .format(a=matrix[0][0], b=matrix[1][1], c=matrix[2][2]))

new_list = []
new_list.append(matrix[0][0])
new_list.append(matrix[1][0])
new_list.append(matrix[2][0])
print(new_list)

#Using  list comprehension
new_list=[row[0] for row in matrix]
print(new_list)