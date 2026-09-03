cnt = 0
b = int(input())
y = 1
while y <= b:
    if b % y == 0:
        cnt+=1
    y+=1
if cnt == 2:
    print("prime")
else:
    print("not prime")