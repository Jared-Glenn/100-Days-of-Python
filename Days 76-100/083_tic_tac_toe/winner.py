
def check_winner(p1, p2):
    winning_combos = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"],
                      ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]

    winner = 0

    for combo in winning_combos:
        if winner > 0:
            break
        in_a_row = 0
        for choice in p1:
            if choice in combo:
                in_a_row += 1
            if in_a_row == 3:
                winner = 1
        in_a_row = 0
        for choice in p2:
            if choice in combo:
                in_a_row += 1
            if in_a_row == 3:
                winner = 2

    return winner
