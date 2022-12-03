from sys import argv

def read_in_file(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    return [line.split(" ") for line in lines]

    # A = Rock = X -> 1
    # B = Paper = Y -> 2
    # C = Sissors = Z -> 3
def convert_to_opponent_value(selection):
    if selection == "X":
        return "A"
    elif selection == "Y":
        return "B"
    elif selection == "Z":
        return "C"

def get_selection_score(selection):
    if selection == "A":
        return 1
    elif selection == "B":
        return 2
    elif selection == "C":
        return 3

# 0 -> loss, 3 -> draw, 6 -> win
def get_win_lose_draw_score(opponent, player):
    win_pairs = [("A", "B"), ("B", "C"), ("C", "A")]
    lose_pairs = [("B", "A"), ("C", "B"), ("A", "C")]
    if opponent == player:
        return 3
    if win_pairs.count((opponent, player)) > 0:
        return 6
    if lose_pairs.count((opponent, player)) > 0:
        return 0

def calculate_total_score(data):
    score = 0
    for pair in data:
        them = pair[0]
        me = pair[1]
        converted_selection = convert_to_opponent_value(me)
        selection_score = get_selection_score(converted_selection)
        win_lose_draw_score = get_win_lose_draw_score(them, converted_selection)
        score = score + selection_score + win_lose_draw_score
    return score

if __name__ == "__main__":
    filename = argv[1]
    data = read_in_file(filename)
    print(calculate_total_score(data))