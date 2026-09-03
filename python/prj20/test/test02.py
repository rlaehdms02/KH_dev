a = [10, 20, 30]
b = [40, 50, None]
c = [70, 80, 90]
table = [a, b, c]
sum_list = 0
found = False
i = 0
for i in range(len(table)):
    if None in table[i]:
        del table[i]
        break
# for item in range(len(table)):
#     for j in range(len(table[item])):
#         if None in table[item][j]:
#             print(f"결축지 : {item}행")
#             del table[item]
#             found = True
#             break
#     if found: break

# for item in range(len(table)):
#     sum = 0
#     for j in range(len(table[item])):
#         sum += table[item][j]
#         table[item][j] = table[item][j] + 1
#     sum_list += sum
#     print(sum_list)
print(f"최종 : {table}")