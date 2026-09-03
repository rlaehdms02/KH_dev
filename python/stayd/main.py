import random
numbers = []
while len(numbers) < 3:
    new_number = random.randint(0, 9)
    if new_number not in numbers:
        numbers.append(new_number)
    print(new_number,end=" ")


print("\n0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
tries = 0
while True:
    new_user_numbers = []
    i = 0

    while i < 3:
        try:
            user_number = int(input(f"{i + 1}번째 숫자를 입력하세요: "))

        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        if user_number < 0 or user_number > 9:
            print("범위를 벗어나는 숫자입니다. 0~9 사이의 숫자를 입력하세요.")
        elif user_number in new_user_numbers:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_user_numbers.append(user_number)
            i += 1
    tries += 1
    strike_count = 0
    ball_count = 0
    for idx in range(3):
        if new_user_numbers[idx] == numbers[idx]:
            strike_count += 1
        elif new_user_numbers[idx] in numbers:
            ball_count += 1
    print(f"\n[결과] {strike_count}S {ball_count}B\n")

    if strike_count == 3:
        print(f"축하합니다! {tries}번 만에 3개의 숫자를 모두 맞히셨습니다.")
        break