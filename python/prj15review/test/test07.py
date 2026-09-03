n = 3
valu = 0
y = []
for i in range(n):
    arr = []
    for j in range(n):
        if i % 2 == 0:
            arr.append(1)
        else:
            arr.append(valu)
    y.append(arr)

print(y)

