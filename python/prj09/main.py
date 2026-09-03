import game.util

while True:
    result = game.util.Q_and_A()
    if result == "종료" or result == "강제 종료" :
        break
    elif result == "재시작":
        continue