from datetime import time

import numpy as np
import time
py_list =[1,2,3,4,5,6]
np_array = np.array([1,2,3,4,5,6])
#리스트
# result_list =[]
# for x in py_list:
#     result= x*2
#     result_list.append(result)
# print(result_list)


#np
# print(np_array*2)

# 속도
# py_list =list(range(1_000_000))
# start_time =time.time()
# result=0
# for x in py_list:
#     result +=x
# end_time =time.time()
# result_time =time =end_time-start_time
# print(result_time)
# print(result)
#============np
np_array =list(range(1_000_000))
result=0
for x in py_list:
    result +=x
start_time =time.time()
result=np.sum(np_array)
end_time =time.time()
result_time =time =end_time-start_time
print(result)
print(result_time)
