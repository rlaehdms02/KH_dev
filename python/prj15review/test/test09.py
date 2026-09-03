y =  []
names = ["심원용","심투용","심삼용"]
subjects = ["수학","영어","과학"]
for i in range(3):
    arr = []
    for j in range(3):
        arr.append(0)
    y.append(arr)

y[0][0] = 80
y[0][1] = 90
y[0][2] = 50
y[1][0] = 30
y[1][1] = 55
y[1][2] = 75
y[2][0] = 35
y[2][1] = 40
y[2][2] = 45
sro = []
one, two, tree = 0, 0, 0
su, eng, sin,  = 0, 0, 0
su_top, eng_top, sin_top = 0, 0, 0
su_idx, eng_idx, sin_idx = 0, 0, 0
for x in range(3):
    print(y[x])
for i in range(3):
    for j in range(3):
        if j == 0:
            su = su + y[i][j]
            if su_top < y[i][0]:
                su_top = y[i][0]
                su_idx = i
        elif j == 1:
            eng = eng + y[i][j]
            if eng_top < y[i][1]:
                eng_top = y[i][1]
                eng_idx = i
        else:
            sin = sin + y[i][j]
            if sin_top < y[i][2]:
                sin_top = y[i][2]
                sin_idx = i
        if i == 0:
            one = one + y[i][j]
        elif i == 1:
            two = two + y[i][j]
        else:
            tree = tree + y[i][j]
sro.append(one)
sro.append(two)
sro.append(tree)
print(sro)
su = su / 3
eng = eng / 3
sin = sin / 3
print(f"수학 : {su:.1f}, 영어 : {eng:.1f}, 과학 : {sin:.1f}")
mvp = 0
loser = sro[0]
idx = -1
for x in range(3):
    print(f"학생별 총점과 평균 : {names[x]}, {sro[x]}, {sro[x]/3:.1f}")
print(f"과목별 최고 점수 해당 학생 수학 :{names[su_idx]}, {su_top} 영어 : {names[eng_idx]}, {eng_top}, 과학 : {names[sin_idx]}, {sin_top}")
for x in range(3):
    if mvp < sro[x]:
        mvp = sro[x]
    elif loser > sro[x]:
        loser = sro[x]
print(f"최고점 : {mvp}, 최저점 {loser}")
for x in range(3):
    if sro[x]/3 < 60:
        print(f"평균 60점 미만 : {sro[x]/3:.1f}")
for i in range(3):
    for j in range(3):
        if y[i][j] <= 40:
            if idx == i:
                continue
            idx = i
            print(f"과락자 : {names[idx]}")
