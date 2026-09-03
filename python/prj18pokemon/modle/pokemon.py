class Pokemon:
    def __init__(self, name, hp, atk,arm):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"

    def tackle(self):
        print("몸통 박치기 ")
    def skill(self):
        print("손가락 흔들기")

class Lizad:
    def __init__(self):
        self.name = "파이리"
        self.hp = 100
        self.atk = 12
        self.arm = 6

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"

class Trutel:
    def __init__(self):
        self.name = "꼬북기"
        self.hp = 120
        self.atk = 7
        self.arm = 8

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"
class Dipsangu():
    def __init__(self):
        self.name = "딥상어둥"
        self.hp = 150
        self.atk = 15
        self.arm = 9

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"

class Pikahun(Pokemon):
    def __init__(self):
        super().__init__("피카츄", 100, 10, 8)

    def __str__(self):
        return f"{self.name} {self.hp} {self.atk}"

