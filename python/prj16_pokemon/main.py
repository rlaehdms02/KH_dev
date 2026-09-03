from model import pikachu, turtle, lizard
from random import randint, random


def batlle(attacker, defender):
    print(f"{attacker.name}가 {defender.name} 를 공격")
    defender.hp -= attacker.akt
    print("attacker : ",attacker)
    print("defender : ", defender)

p1 = pikachu.Pikachu()
p2 = turtle.Turtle()
p3 = lizard.Lizard()

print("===== pokemon =====")
print("1", p1)
print("2", p2)
print("3", p3)
print()

num = int(input("원하는 포켓몬 번호 : "))

match num:
    case 1:
        user = pikachu.Pikachu()
    case 2:
        user = turtle.Turtle()
    case 3:
        user = lizard.Lizard()

num = randint(1, 3)
match num:
    case 1:
        com = pikachu.Pikachu()
    case 2:
        com = turtle.Turtle()
    case 3:
        com = lizard.Lizard()

while True:
    batlle(user, com)
    if com.hp <= 0:
        break
    batlle(com, user)
    if user.hp <= 0:
        break
