from sys import argv

def get_directions(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    data = [x.split(" ") for x in data]
    return [[x[0],int(x[1])] for x in data]

def is_positive(int):
    return int > 0

def is_negative(int):
    return int < 0

def new_tail_location(H, T):
    path = {"00"}
    while abs(H[0]-T[0]) > 1 or abs(H[1] - T[1]) > 1:
        if H[0] > T[0]: 
            T[0] += 1
        if H[1] > T[1]: 
            T[1] += 1
        if H[0] < T[0]:
            T[0] += -1
        if H[1] < T[1]: 
            T[1] += -1
        path.add(str(T[0]) + str(T[1]))
    return T, path

def get_positions_visited(instructions):
    visited = {"00"}
    H = [0,0]
    T = [0,0]
    rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    for instruction in instructions:
        left_or_right = instruction[0] == "L" or instruction[0] == "R"
        if instruction[0] == "D" or instruction[0] == "L":
            direction = -1
        else:
            direction = 1 
        if left_or_right:
            H[0] = H[0] + (instruction[1] * direction)
        else:
            H[1] = H[1] + (instruction[1] * direction)
        rope[0] = H
        loop_count = 9
        for i in range(loop_count):
            T, path = new_tail_location(rope[i], rope[i+1])
            rope[i+1] = T
        visited.update(path)
    return visited

if __name__ == "__main__":
    filename = argv[1]
    directions = get_directions(filename)
    grid = get_positions_visited(directions)
    print("result: " + str(len(grid)))

# too high 2478
# too low 2439