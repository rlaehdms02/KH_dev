class Pokemon:
    def __init__(self, name, hp, akt):
        self.name = name
        self.hp = hp
        self.akt = akt

    def __str__(self):
        return f"{self.name} {self.hp} {self.akt}"

class Lizard:
    def __init__(self):
        self.name = "파이리"
        self.hp = 80
        self.akt = 12
    def __str__(self):
        return f"{self.name} {self.hp} {self.akt}"

class Turtle:
    def __init__(self):
        self.name = "꼬부기"
        self.hp = 70
        self.akt = 7
    def __str__(self):
        return f"{self.name} {self.hp} {self.akt}"
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("피카츄" ,100, 10)
    def __str__(self):
        return f"{self.name} {self.hp} {self.akt}"