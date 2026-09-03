n = 3
valu = 0
y = []
for i in range(n):
    arr = []
    for j in range(n):
        if i == j:
            arr.append(1)
        else:
            arr.append(valu)
    y.append(arr)

print(y)

y =[]
for i in range(n):
    y.append([])
    for j in range(n):
        y[i].append(1)
print(y)