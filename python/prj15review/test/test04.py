z, x = map(int, input().split())
y = []
cnt = 1
for i in range(z):
    arr = []
    for j in range(x):
        arr.append(cnt)
        cnt += 1
    y.append(arr)


print(y)