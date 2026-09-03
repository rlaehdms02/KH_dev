import  random

def Q_and_A():
    Q = ["cd", "pwd", "vi", "su", "sudo"]
    tr, b, c = map(int, input().split(", "))
    A = random.sample(Q, 3)
    i = 0
    cnt = 0
    len(Q)-len(A)
    for i in A:
        if i == "cd":
            print("현재 작업 중인 폴더(디렉토리)를 이동할 때 사용 명령어는 ?")
            QA = input().lower()
            if QA == i:
                print("정답입니다.")
                cnt += 1
            else:
                print(f"정답은 {i}입니다.")
        if i == "pwd":
            print("현재 사용자가 작업 중인 디렉터리의 절대 경로를 터미널 화면에 출력하는 명령어는 ?")
            QA = input().lower()
            if QA == i:
                print("정답입니다.")
                cnt += 1
            else:
                print(f"정답은 {i}입니다.")
        if i == "vi":
            print("터미널 환경에서 텍스트 파일을 생성하고 수정하는 명령어는 ? ")
            QA = input().lower()
            if QA == i:
                print("정답입니다.")
                cnt += 1
            else:
                print(f"정답은 {i}입니다.")
        if i == "su":
            print("현재 계정을 로그아웃하지 않고 다른 사용자의 권한으로 전환하거나 셸을 실행하는 명령어는 ?")
            QA = input().lower()
            if QA == i:
                print("정답입니다.")
                cnt += 1
            else:
                print(f"정답은 {i}입니다.")
        if i == "sudo":
            print("일반 사용자가 최고 관리자(root) 권한을 일시적으로 빌려 특정 명령어를 실행하게 해주는 명령어는 ?")
            QA = input().lower()
            if QA == i:
                print("정답입니다.")
                cnt += 1
            else:
                print(f"정답은 {i}입니다.")
    if cnt == 3:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 1:
        print("C")
    else:
        print("F")
    print(f"정답 수 :{cnt}")
    print("다시 시작하실꺼면 Y 또는 y 그만하실꺼면 X 또는 x를 눌러주세요.")
    QA_redstart = input().lower()
    if QA_redstart == "y":
        print("재시작")
        cnt = 0
        return  "재시작"
    elif QA_redstart == "n":
        print("종료")
        return "종료"
    else:
        print("강제 종료")
        return "강제 종료"