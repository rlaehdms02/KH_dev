import random

def RSP_games():
    while True:
        print("가위 바위 보 게임을 시작합니다.")
        RSP_list = ["가위","바위","보"]
        set_RSP = random.choice(RSP_list)
        user_RSP = input("가위, 바위, 보 중 하나를 입력해주세요. 또는 숫자 1, 2, 3을 입력해주세요.")
        if set_RSP == "가위" and (user_RSP == "바위" or user_RSP == "2") or set_RSP == "바위" and (user_RSP == "보" or user_RSP == "3") or set_RSP == "보" and (user_RSP == "가위" or user_RSP == "1"):
            print(f"컴퓨터 : {set_RSP}")
            print("승리하셨습니다.")
        else:
            print(f"컴퓨터 : {set_RSP}")
            print("졌습니다.")
        break