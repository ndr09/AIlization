import numpy as np


class Grid():
    gbound = None
    reward = dict()
    rng = None
    units = [dict(), dict()]

    def __init__(self, n, number_reward, seed):
        assert n > number_reward - 2
        self.rng = np.random.default_rng(seed)
        self.gbound = (-(n // 2), n // 2)
        while len(self.reward.keys()) <= number_reward:
            self.reward[(self.rng.integers(-(n // 2), n // 2), self.rng.integers(-(n // 2), n // 2))] = 1

    def __str__(self):
        return str(self.reward)

    def resolve_combat(self, pos, attacker, attacker_pos, attacker_player):
        defender = self.units[(attacker_player + 1) % 2][pos]
        defender.life -= attacker.attack
        if defender.life <= 0:
            self.units2.pop(pos)
            return self.move_units(attacker_player, attacker, attacker_pos, pos)
        else:
            attacker.life -= defender.life
            attacker.movement = 0
            if attacker.life <= 0:
                self.units[attacker_player].pop(attacker_pos)
                return -3
            return 0

    def calculate_dist(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]

        if np.sign(dx) == np.sign(dy):
            return abs(dx + dy)
        else:
            return max(abs(dx), abs(dy))

    def move_units(self, player, pos, new_pos):
        unit = self.units[player][pos]
        if self.calculate_dist(pos, new_pos) > unit.movement or not self.valide_move(new_pos):
            return -1

        if new_pos in self.units[player]:
            return -2

        if new_pos in self.units[(player + 1) % 2]:
            return self.resolve_combat(new_pos, unit, pos, player)

        unit.movement = 0
        self.units[player].pop(pos)
        self.units[player][new_pos] = unit

        if new_pos in self.reward:
            return self.reward.pop(new_pos)
        return 0

    def insert_unit(self, player, unit):
        if unit.pos not in self.units[player]:
            self.units[player][unit.pos] = unit
            return 0
        else:
            return -1

    def is_valide_move(self, pos):
        if (self.gbound[0] <= pos[0] <= self.gbound[1]) and (self.gbound[0] <= pos[1] <= self.gbound[1]):
            return True
        else:
            return False
