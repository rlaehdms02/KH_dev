x, y = map(int, input().split())
try:
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Division by zero")
print("finish")