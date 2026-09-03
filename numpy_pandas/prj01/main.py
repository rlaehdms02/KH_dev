scores = [80,85,70,90]
# temp = []
# for i in scores:
#     temp.append(i + 5)
# scores = temp
print(scores)

total = 0
for i in scores:
    total = total + i
avg = total / len(scores)
print(total)
print(avg)