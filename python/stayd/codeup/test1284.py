import math
a = int(input())
doc_max = 0
doc_min = 0
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, a):
    if a % i == 0:
        other = a // i
        if is_prime(i) and is_prime(other):
            if i <= other:
                doc_min = i
                doc_max = other
            else:
                doc_min = other
                doc_max = i
            break
if doc_min > 1 and doc_max > 1:
    print(f"{doc_min} {doc_max}")
else:
    print("wrong number")

