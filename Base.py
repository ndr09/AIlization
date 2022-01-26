from Units import *


class Base():
    points = 0
    pos = None
    id = ""

    def __init__(self, pos, id):
        self.points = 0
        self.pos = pos
        self.id = id

    def __str__(self):
        return "player id: " + str(self.id) + " points: " + str(self.points)

    def base_produce_unit(self, unit_id):
        unit = None
        if unit_id == 0:
            tmp = Scout()
            print(tmp.cost)
            print(self.points)
            unit = tmp if tmp.cost <= self.points else None
        if unit_id == 1:
            unit = Warrior() if Warrior().cost <= self.points else None
        if unit_id == 2:
            unit = Knight() if Knight().cost <= self.points else None
        print(unit)
        unit.set_pos(self.pos)
        return unit
