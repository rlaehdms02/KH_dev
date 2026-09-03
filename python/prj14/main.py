a  = list(range(3))
b  = list(range(3))
c  = list(range(3))

x = [a, b ,c ]
v =  10
i = 0
while i < 3:
    idx = 0
    while idx < 3:
        x[i][idx] = v
        v += 10
        idx += 1
    i += 1

print(x)