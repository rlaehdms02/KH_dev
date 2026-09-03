
y =  []
names = ["심원용","심투용","심삼용"]
subjects = ["수학","영어","과학"]
for i in range(3):
    arr = []
    for j in range(3):
        arr.append(0)
    y.append(arr)

y[0][0] = 80
y[0][1] = 90
y[0][2] = 50
y[1][0] = 70
y[1][1] = 55
y[1][2] = 75
y[2][0] = 85
y[2][1] = 40
y[2][2] = 45

for x in range(3):
    print(y[x])
idx = -1
total_list = []
for i in range(3):
    total = 0
    for score in y[i]:
        total += score
    total_list.append(total)
print(total_list)
top = 0
for i  in range(3):
    if top < total_list[i]:
        top = total_list[i]
        idx = i
top = max(total_list)
print(f"top = {top}, idx = {idx}, name : {names[idx]}")
print(top)