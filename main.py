from Grid import Grid
from Base import Base
import Units


# Press the green button in the gutter to run the script.

class Environment():
    grid = None
    players = []
    turn = 0

    def __init__(self, size, points, turn_limit):
        self.grid = Grid(size, points, 0)
        self.players.append(Base((-(size // 2), 0), "p1"))
        self.players.append(Base(((size // 2), 0), "p2"))
        self.turn = turn_limit

    def check_victory(self):
        if self.players[0].points == 0 and len(self.grid.units[0].keys()) == 0:
            return 1
        if self.players[1].points == 0 and len(self.grid.units[1].keys()) == 0:
            return 2
        if self.turn == 0:
            points_p1 = self.players[0].points + sum([u.cost for u in self.grid.units[0]])
            points_p2 = self.players[1].points + sum([u.cost for u in self.grid.units[1]])
            if points_p1 > points_p2:
                return -1
            elif points_p2 > points_p1:
                return -2
            return 3

        return 0

    def get_info(self, player):
        return self.grid.units[player], self.grid.reward

    def make_turn(self, player1_move, player2_move):
        mv_results = [[],[]]
        for unit1 in player1_move:
            if len(unit1) == 2:
                mv_results[0].append(self.grid.move_units(0, unit1[0], unit1[1]))
            elif len(unit1) == 1:
                mv_results[0].append(self.grid.insert_unit(0, unit1[0]))

        for unit1 in player2_move:
            if len(unit1) == 2:
                mv_results[1].append(self.grid.move_units(1, unit1[0], unit1[1]))
            elif len(unit1) == 1:
                mv_results[1].append(self.grid.insert_unit(1, unit1[0]))
        self.turn -= 1
        return self.check_victory(), mv_results


if __name__ == '__main__':
    grid = Grid(7, 5, 0)
    p1 = Base((-3, 0), "p1")
    p2 = Base((3, 0), "p2")
    u = p1.base_produce_unit(0)
    grid.insert_unit(0, u)
    print(grid)
