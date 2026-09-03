from games.ltto import lotto_game
from games.RSPgame import RSP_games
from games.up_down import  up_down_game
while True:
    print("1. 업다운")
    print("2. 가위바위보")
    print("3. 로또 번호 맞추기")
    print("4. 종료")

    menu = int(input("메뉴 선택 : "))
    if menu == 1:
        up_down_game()
    elif menu == 2:
        RSP_games()
    elif menu == 3:
        lotto_game()
    elif menu == 4:
        break