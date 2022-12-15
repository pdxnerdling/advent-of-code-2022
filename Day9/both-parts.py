from sys import argv

LENGTH = 1

def get_directions(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    data = [x.split(" ") for x in data]
    return [[x[0],int(x[1])] for x in data]

def is_positive(int):
    return int > 0

def is_negative(int):
    return int < 0

def new_tail_location(H, T, i):
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
    rope = [ [0,0] for _ in range(LENGTH + 1) ]
    for instruction in instructions:
        #print(instruction)
        if instruction[0] == "D" or instruction[0] == "L":
            direction = -1
        else:
            direction = 1 
        if instruction[0] == "L" or instruction[0] == "R":
            H[0] = H[0] + (instruction[1] * direction)
        else:
            H[1] = H[1] + (instruction[1] * direction)
        for _ in range(instruction[1]):
            if instruction[0] == "D":
                rope[0][1] = rope[0][1] + -1
            if instruction[0] == "U":
                rope[0][1] = rope[0][1] + 1
            if instruction[0] == "L":
                rope[0][0] = rope[0][0] + -1
            if instruction[0] == "R":
                rope[0][0] = rope[0][0] + 1
            for i in range(LENGTH):
                T, path = new_tail_location(rope[i], rope[i+1], i)
                rope[i+1] = T
            visited.update(path)
    return visited

if __name__ == "__main__":
    filename = argv[1]
    LENGTH = int(argv[2])
    directions = get_directions(filename)
    visit_count = get_positions_visited(directions)
    print("Rope Length " + str(LENGTH) +" Result: " + str(len(visit_count)))