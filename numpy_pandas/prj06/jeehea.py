import numpy as np

# 10일 동안의 '혜성전자' 주식 종가 (단위: 원)
prices = np.array([50000, 52000, 49000, 55000, 58000, 57000, 62000, 59000, 64000, 63000])

# 1. 이 주식을 가장 쌀 때 사서 가장 비쌀 때 팔았다면, 1주당 얻을 수 있는 '최대 수익금'은 얼마인가요?
result1 = np.argmin(prices)
result2 = np.argmax(prices[result1:])
result3 = prices[result2+result1] - prices[result1]
print(result3)
# 2. 전날과 비교해서 주가가 가장 많이 떨어진(하락폭이 가장 큰) 날은 전날 대비 얼마가 떨어졌나요?
diff = np.diff(prices)
max_drop = np.min(diff)
result4 = abs(max_drop)
print(result4)
# 3. 주가가 6만 원 이상이었던 날은 10일 중 총 며칠이나 되나요?
result5 = np.sum(prices >= 60000)
print(result5)
# 4. 주가가 '전체 평균 주가'보다 낮았던 우울한 날들만 따로 모아서 보면, 그날들의 평균 주가는 얼마인가요?
result6 = prices < np.mean(prices)
print(prices[result6])
# 5. 주가가 6만 원을 넘긴 기분 좋은 날들의 '인덱스(몇 번째 위치인지)'를 모두 찾아주세요
result7 = np.sort(np.where(prices > 60000))
print(result7)