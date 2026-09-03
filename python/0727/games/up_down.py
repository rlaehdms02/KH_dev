import random

def up_down_game():
    random_num = random.randint(1,100)
    i = 0
    while True:
        set_number = int(input("1~100중 하나의 숫자를 입력하세요."))
        if set_number > random_num:
            i += 1
            print("DOWN")
        elif set_number < random_num:
            i+= 1
            print("UP")
        else:
            i += 1
            print(f"축하합니다. {i}번째 맞추셨습니다.")
            break