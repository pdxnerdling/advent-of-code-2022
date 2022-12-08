from sys import argv
from functools import reduce

def get_file_size(line):
    split = line.split(" ")
    return int(split[0])

def get_size_next_dir(terminal_output, dir_sizes):
    dir_size = 0
    go = True
    while(go):
        if len(terminal_output) == 0:
            break
        command = terminal_output.pop()
        if command[0] == "$":
            if command.count("cd ..") > 0:
                go = False
            elif command.count("cd ") > 0 and command.count("cd ..") == 0:
                prev_dir_size, dir_sizes= get_size_next_dir(terminal_output, dir_sizes)
                dir_size += prev_dir_size
        elif command[0].isnumeric():
            dir_size += get_file_size(command)
    dir_sizes.append(dir_size)
    return dir_size, dir_sizes

def traverse_directories(terminal_output):
    total_size, dir_sizes = get_size_next_dir(terminal_output, [])
    return dir_sizes   

def get_directories_with_sizes(filename):
    f = open(filename, 'r')
    terminal_output = f.read().splitlines()
    terminal_output.reverse()
    return traverse_directories(terminal_output)

def calculate_part1(dir_sizes):
    dir_sizes.sort()
    sum_under_100000 = 0
    for size in dir_sizes:
        if size <= 100000:
            sum_under_100000 += size
    print("Part 1: " + str(sum_under_100000))

def calculate_part2(dir_sizes):
    dir_sizes.sort(reverse=True)
    largest = dir_sizes[0]
    needed_space = 30000000 - (70000000 - largest)
    go = True
    i = 0
    while(go):
        if dir_sizes[i+1] < needed_space:
            print("Part 2: " + str(dir_sizes[i]))
            go = False
        i += 1
        if i >= len(dir_sizes):
            go = False

if __name__ == "__main__":
    filename = argv[1]
    dir_sizes = get_directories_with_sizes(filename)
    calculate_part1(dir_sizes)
    calculate_part2(dir_sizes)