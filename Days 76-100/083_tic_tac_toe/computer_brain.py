from random import shuffle, choice


def computer_brain(p1, p2, available):
    winning_combos = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"],
                      ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]

    shuffle(winning_combos)
    good_moves = []

    for combo in winning_combos:
        for space in p1:
            if space in combo and winning_combos:
                winning_combos = winning_combos.remove(combo)

    if not winning_combos:
        return choice(available)
    else:
        for combo in winning_combos:
            for space in combo:
                if space in available:
                    good_moves.append(space)

    for combo in winning_combos:
        for space in p2:
            if space not in combo and winning_combos:
                winning_combos = winning_combos.remove(combo)

    if not winning_combos:
        return choice(good_moves)
    else:
        good_moves = []
        for combo in winning_combos:
            for space in combo:
                if space in available:
                    good_moves.append(space)

    return choice(good_moves)