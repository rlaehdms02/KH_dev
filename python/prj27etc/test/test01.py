matrix = [[1,2,],[3,4]]
# x = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         x.append(matrix[row][col])
#     print(x)

result = [v**2 for row in matrix for v in row]
print(result)