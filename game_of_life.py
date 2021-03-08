import colorama
from colorama import Fore
import random
import time

colorama.init(autoreset=True)


def print_universe(universe_resurrected):
    epochal_output = ''

    for line in universe_resurrected:

        for nom in line:

            if nom == 0:
                epochal_output += Fore.BLACK + '-'
            elif nom == 1:
                epochal_output += Fore.YELLOW + '∴'
            else:
                epochal_output += '😱'

        epochal_output += '\n'

    print(epochal_output)


def create_universe(universe_width, universe_height):
    universe = []

    for y in range(universe_height):
        row = []

        for x in range(universe_width):
            row.append(0)

        universe.append(row)

    return universe


def populate_universe(universe, random_life):
    universe_resurrected = []

    for y in range(len(universe)):
        row = []

        for x in range(len(universe[y])):

            if random.randrange(0, 100) < random_life:
                universe[y][x] = 1

            row.append(universe[y][x])
        universe_resurrected.append(row)
    return universe_resurrected


def n(universe_resurrected, y, x):
    return universe_resurrected[y - 1][x]


def ne(universe_resurrected, y, x):
    if x + 1 >= len(universe[y]):
        return 0
    return universe_resurrected[y - 1][x + 1]


def e(universe_resurrected, y, x):
    if x + 1 >= len(universe[y]):
        return 0
    return universe_resurrected[y][x + 1]


def se(universe_resurrected, y, x):
    if y + 1 >= len(universe):
        return 0
    if x + 1 >= len(universe[y]):
        return 0
    return universe_resurrected[y + 1][x + 1]


def s(universe_resurrected, y, x):
    if y + 1 >= len(universe):
        return 0
    return universe_resurrected[y + 1][x]


def sw(universe_resurrected, y, x):
    if y + 1 >= len(universe):
        return 0
    return universe_resurrected[y + 1][x - 1]


def w(universe_resurrected, y, x):
    return universe_resurrected[y][x - 1]


def nw(universe_resurrected, y, x):
    return universe_resurrected[y - 1][x - 1]


universe = create_universe(120, 120)
universe = populate_universe(universe, 20)

while True:

    print_universe(universe)
    time.sleep(.1)

    zeros_for_a_new_epoch = create_universe(120, 120)

    for y in range(len(universe)):

        for x in range(len(universe[y])):

            n_state = n(universe, y, x)
            ne_state = ne(universe, y, x)
            e_state = e(universe, y, x)
            se_state = se(universe, y, x)
            s_state = s(universe, y, x)
            sw_state = sw(universe, y, x)
            w_state = w(universe, y, x)
            nw_state = nw(universe, y, x)

            current_noms_surroundings = [n_state, ne_state, e_state, se_state, s_state, sw_state, w_state, nw_state]
            noms_summed = sum(current_noms_surroundings)

            #  underpopulation
            if universe[y][x] == 1:
                if noms_summed < 2:
                    zeros_for_a_new_epoch[y][x] = 0

            #  stasis
            if universe[y][x] == 1:
                if noms_summed == 2 or noms_summed == 3:
                    zeros_for_a_new_epoch[y][x] = 1

            #  genesis
            if universe[y][x] == 0:
                if noms_summed == 3:
                    zeros_for_a_new_epoch[y][x] = 1

            #  overpopulation
            if universe[y][x] == 1:
                if noms_summed > 3:
                    zeros_for_a_new_epoch[y][x] = 0

    universe = zeros_for_a_new_epoch

    if random.randrange(0, 100) > 80:
        for i in range(0, 100):
            p = random.randrange(0, len(universe))
            q = random.randrange(0, len(universe[0]))
            universe[p][q] = 1

    if random.randrange(0, 100) > 80:
        for i in range(0, 100):
            p = random.randrange(0, len(universe))
            q = random.randrange(0, len(universe[0]))
            universe[p][q] = 0
