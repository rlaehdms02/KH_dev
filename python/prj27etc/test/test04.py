name = ["홍길동", "임꺽정", "김철수"]
scores = [100,200,300]
height = [180,190,170]

result = zip(name, scores, height)
for n, s, h in result:
    print(f"{n} / {s} / {h}")
