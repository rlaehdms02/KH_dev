a, b = map(int, input().split())
a_sum = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        print(f"-{i}",end="")
        a_sum = a_sum - i
    else:
        if i == a:
            print(f"{i}",end="")
        else:
            print(f"+{i}", end="")
        a_sum = a_sum + i
print(f"={a_sum}")

