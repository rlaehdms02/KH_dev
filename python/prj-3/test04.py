#list : 순서 있음, 변경가능, 중복 허요으 다양한 타입
x = ["사과", "딸기", 3.14, 100, True, "계란"]

#print(x)
#print(x[0])
#x[0] = "바나나"
#print(x[0])

x.append(777)
print(x)

x.insert(2, "홍진호")

print(x)

x.remove(777)
print(x)

#x.clear()

y = ["박혜린", "박하솔", "이상식" , "콩진호", "콩진호", "콩진호", "콩진호"]
x.extend(y)
print(x)

i = x.index("박하솔")
print(i)

cnt = x.count("콩진호")
print(cnt)

#temp = x.sort()
#print(x)

x.reverse()
print(x)

x2 = x
x[0] = "임요한"
print(x)
print(x2)
x2[0] = "test"
print(x2)
print(x)

i = 0