x  = []
value = 10
for i in range(3):
    temp = []
    for j in range(3):
        test = []
        temp.append(value)
        value += 10
        for z in range(3):
            test.append(value)
            value += 10
    x.append(test)

print(x)
print(temp)