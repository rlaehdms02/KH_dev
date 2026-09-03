import random

def lotto_game():
    set_lotto = random.sample(range(1, 46), 6)
    us_lotto_list = []
    set_lotto.sort()
    while len(us_lotto_list) < 6:
        lotto = int(input(f"{len(us_lotto_list) + 1}번째 번호 : "))
        if lotto > 45 or lotto < 1:
            print("1~45 값 하나를 입력하세요.")
        elif lotto in us_lotto_list:
            print("이미 입력한 숫자입니다. 중복 없이 입력해주세요.")
        else:
            us_lotto_list.append(lotto)
    us_lotto_list.sort()
    print(f"당첨 번호 : {set_lotto}")
    print(f"내 번호 : {us_lotto_list}")
    matched_number = set(set_lotto) & set(us_lotto_list)
    print(f"맞춘 개수 : {len(matched_number)}개")
    if len(matched_number) == 6:
        print("축하합니다 1등 입니다.")
    elif len(matched_number) == 6:
        print("축하합니다 2등 입니다.")
    elif    len(matched_number) == 6:
        print("축하합니다 3등 입니다.")
    elif    len(matched_number) == 6:
        print("축하합니다 4등 입니다.")
    elif    len(matched_number) == 6:
        print("축하합니다 5등 입니다.")
    else:
        print("아쉽게도 꽝입니다.")