from random import randint

from manager import play_game
from modle import pokemon
play_game()
def battle(attacker, defender):
    print(f"{attacker.name}가 {defender.name}을 공격했습니다.")
    defender.hp= defender.hp - (attacker.atk * 1.5 - defender.arm)

def miss(attacker):
    print(f"{attacker.name}가 공격했으나 빗나갔다.")

def critical(attacker, defender):
    print(f"{attacker.name}가 {defender.name}을 공격했습니다.")
    print("급소에 맞았다.")
    print(f"{attacker}\n{defender}")
    defender.hp= defender.hp - ((attacker.atk * 1.5)*1.5- defender.arm)

print("=====포켓몬 리스트=====")
print(f"1. {pokemon.Pikahun()}")
print(f"2. {pokemon.Lizad()}")
print(f"3. {pokemon.Trutel()}")
print(f"4. {pokemon.Dipsangu()}")

num = int(input())

match num:
    case 1:
        user = pokemon.Pikahun()
    case 2:
        user = pokemon.Lizad()
    case 3:
        user = pokemon.Trutel()
    case 4:
        user = pokemon.Dipsangu()
num = randint(1,3)

match num:
    case 1:
        cpu = pokemon.Pikahun()
    case 2:
        cpu = pokemon.Lizad()
    case 3:
        cpu = pokemon.Trutel()
    case 4:
        cpu = pokemon.Dipsangu()
cnt = 0
num = 0
cri = 0
while True:
    num = randint(1,10)
    cri = randint(1,10)
    if cnt == 0:
        if num >= 8:
            cnt = 1
            miss(user)
            continue
        elif cri >= 9:
            critical(user,cpu)
            cnt = 1
            continue
        battle(user,cpu)
        cnt = 1
    elif cnt == 1:
        if num >= 8:
            miss(cpu)
            cnt = 0
            continue
        elif cri >= 9:
            critical(cpu,user)
            cnt = 0
            continue
        battle(cpu,user)
        cnt = 0
    if cpu.hp <= 0:
        print("배틀에서 이겼습니다.")
        break
    if user.hp <= 0:
        print("배틀에서 졌습니다.")
        break
    print(f"사용자 : {user}")
    print(f"컴퓨터 : {cpu}")


