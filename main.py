from Grid import Grid
from Base import Base
import Units
from hexalattice.hexalattice import *
from matplotlib import pyplot as plt


# Press the green button in the gutter to run the script.

class Environment():
    grid = None
    players = []
    turn = 0
    turn_limit = 0
    map_size = 0

    def __init__(self, size, points, turn_limit):
        self.grid = Grid(size, points, 0)
        self.map_size = size
        self.players.append(Base((-(size // 2), 0), "p1"))
        self.players.append(Base(((size // 2), 0), "p2"))
        self.turn = turn_limit
        self.turn_limit = turn_limit

    def __str__(self):

        return str(self.players[0]) + "\n" + str(self.players[1]) + "\nturn: " + str(
            self.turn_limit - self.turn) + "/" + str(self.turn_limit)

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

    def make_turn(self, player1_move, player2_move, update=True):
        mv_results = [[], []]
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

        if not update:
            return self.check_victory(), mv_results

        self.turn -= 1
        return self.check_victory(), mv_results
    def from_xy_to_i(self, pos):
        r = pos[0]+(self.map_size//2)
        c = pos[1]+(self.map_size//2)
        return r*self.map_size+c

    def plot_grid(self):


        hex_centers, _ = create_hex_grid(nx=self.map_size,
                                         ny=self.map_size,
                                         do_plot=False)
        x_hex_coords = hex_centers[:, 0]
        y_hex_coords = hex_centers[:, 1]
        ec = [ (1., 1., 1.) for i in range(len(x_hex_coords))]
        fc = [(0., 0., 0.) for i in range(len(x_hex_coords))]
        ec[6] = (0., 0.5, 0.5)
        fc[6] = (1., 0., 0.)
        plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,
                                          face_color=ec,
                                          edge_color=fc,
                                          min_diam=1.0,
                                          plotting_gap=0.02,
                                          rotate_deg=0)
        plt.savefig("test.png")

if __name__ == '__main__':
    env = Environment(7, 5, 10)
    env.plot_grid()
    print(env)
