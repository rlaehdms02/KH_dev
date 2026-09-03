result = [] # 홀 또는 짝
# for x in range(10):
#     if x % 2 == 0:
#         result.append("짝")
#     else:
#         result.append("홀")
# print(result)

result = ["짝" if n % 2 ==0 else "홀" for n in range(10)]
print(result)