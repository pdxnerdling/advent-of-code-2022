from sys import argv

def read_in_file(filename):
    f = open(filename, 'r')
    lines = f.read().splitlines()
    return [line.split(" ") for line in lines]

def get_win_lose_draw_info(opponent_selection, direction):
    # opponent_choice : player_choice
    win_pairs = {"A":"B", "B":"C", "C":"A"}
    lose_pairs = {"B":"A", "C":"B", "A":"C"}
    if direction == "Y": # need to draw
        return (opponent_selection, 3)
    if direction == "Z": # need to win
        select = win_pairs.get(opponent_selection)
        return (select, 6)
    if direction == "X": # need to lose
        select = lose_pairs.get(opponent_selection)
        return (select, 0)

def get_selection_score(selection):
    # A = Rock -> 1
    # B = Paper -> 2
    # C = Sissors -> 3
    if selection == "A":
        return 1
    elif selection == "B":
        return 2
    elif selection == "C":
        return 3

def calculate_total_score(data):
    opponent_choice = 0
    direction = 1
    score = 0
    for pair in data:
        win_lose_draw_info = get_win_lose_draw_info(pair[opponent_choice], pair[direction])
        selection_score = get_selection_score(win_lose_draw_info[opponent_choice])
        score = score + selection_score + win_lose_draw_info[direction]
    return score

if __name__ == "__main__":
    filename = argv[1]
    data = read_in_file(filename)
    print(calculate_total_score(data))