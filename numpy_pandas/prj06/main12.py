import numpy as np
# 입출금 내역 (양수=입금, 음수=출금)
trans = np.array([100, -30, 50, -80, 200, -60])

# 1. 거래별 누적 잔액 (시작 잔액 0)
result1 = np.cumsum(trans)
print(result1)
# 2. 최종 잔액
result2 = np.sum(trans)
print(result2)
# 3. 잔액이 가장 많았던 시점의 잔액
result3 = np.max(result1)
print(result3)
# 4. (도전) 잔액이 마이너스가 된 적이 있는가?