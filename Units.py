class Unit():
    life = 0
    movement = 0
    attack = 0
    cost = 0
    pos = None


    def set_pos(self, pos):
        self.pos = pos


class Scout(Unit):
    def __init__(self):
        self.life = 20
        self.movement = 4
        self.attack = 5
        self.cost = 1
    def __str__(self):
        return "scout life "+str(self.life)+" mov "+str(self.movement)

class Warrior(Unit):
    def __init__(self):
        self.life = 40
        self.movement = 2
        self.attack = 10
        self.cost = 2
    def __str__(self):
        return "warrior life "+str(self.life)+" mov "+str(self.movement)

class Knight(Unit):
    def __init__(self):
        self.life = 30
        self.movement = 4
        self.attack = 10
        self.cost = 3
    def __str__(self):
        return "Knight life "+str(self.life)+" mov "+str(self.movement)