import numpy as np

A = np.array([[2, 1],
              [1, 3]])
B = np.array([[1, 0],
              [2, 1]])

# 1. 요소별 곱  A * B
c = A*B
print(c)
# 2. 행렬곱    A @ B
d = A @ B
print(d)
# 3. A의 역행렬
inv = np.linalg.inv(A)
print(inv)
# 4. (도전) 연립방정식 풀기
A_eq = np.array([[2, 1],
                 [1, 3]])
b_eq = np.array([5, 10])

solution = np.linalg.solve(A_eq, b_eq)
print(f"4. 연립방정식 해 (solve): x = {solution[0]}, y = {solution[1]}")
#    2x + y = 5
#     x + 3y = 10