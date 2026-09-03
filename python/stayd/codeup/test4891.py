i = int(input())
score = []
score = list(map(int, input().split()))
z = 0
max = score[0]
min = score[0]
for z in range(len(score)):
    if max < score[z]:
        max = score[z]
    if min > score[z]:
        min = score[z]
print(max-min)
