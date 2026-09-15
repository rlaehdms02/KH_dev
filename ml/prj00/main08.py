#퍼셉트론 ,MLP
import numpy as np
def step(x):
    if x> 0:
        return 1
    else:
        return 0
def perceptron(x,w,b):
    z=np.dot(x,w)+b
    y=step (z)
    return y

def AND(x1,x2):
    y= perceptron(np.array([x1,x2]),np.array([0.5,0.5]),-0.9)
    return y
def OR(x1,x2):
    y= perceptron(np.array([x1,x2]),np.array([0.5,0.5]),-0.4)
    return y
def NAND(x1,x2):
    y=not AND(x1,x2)
    return int(y)
def XOR(x1,x2):
    t1 =NAND(x1,x2)
    t2=OR(x1,x2)
    y=AND(t1,t2)
    return y

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))

print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))

# def step(x):
#     if x>0:
#         return 1
#     else:
#         return 0
# def perceptron(x1,x2,x3):
#     result =w1*x1 +w2*x2+w3*x3+b
#     y=#판단을 도와주는 함수
#     return y
# x=np.array([1,1])#입력값

# w=np.array([0.5,0.5])#가중치
# b=-0.9#편향
#
# z=np.dot(x,w)+b
# y=step(z)
#
# print(y)
# print(z)