#numpy 사용 이유 list보다 계산이 편리해서
#리스트 : 타입 제한 x
#넘파이 : 한가지 타입
#넘파이란 ? 같은 종류의 데이터를 한꺼번에 계산할 때 유용하다
import numpy as np

a = [1,2,3,4,5]
b = np.array(a)
print(a)
print(b*10)