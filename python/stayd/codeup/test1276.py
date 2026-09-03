a = int(input())
fak_sum = a
for i in range(a+1):
    a=a-1
    if a == 0:
        break
    else:
        fak_sum = fak_sum * a

print(f"{fak_sum}")