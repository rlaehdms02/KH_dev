n = int(input())
x = []
valu = 1
for i in range(n):
    arr = [1]
    for j in range(n):
        arr.append(valu)
    x.append(arr)
print(x)