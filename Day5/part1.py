from functools import reduce
from sys import argv

def parse_data(filename):
    f = open(filename, 'r')
    data = f.read().splitlines()
    stacks = []
    instructions = []
    line = data.pop()
    while line != "":
        instructions.append(line.replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
        line = data.pop()
    columns = list(data.pop())
    num_columns = int(columns[len(columns)-2])
    stacks = [[] for x in range(num_columns)]
    while len(data) > 0:
        line = data.pop()
        for x in range(1, num_columns+1):
            if line[columns.index(str(x))] != " ":
                stacks[x-1].append(line[columns.index(str(x))])
    return instructions, stacks

def get_top_containers(instructions, stacks):
    instructions.reverse()
    for instruction in instructions:
        num = int(instruction[0])
        start = int(instruction[1]) - 1
        to = int(instruction[2]) - 1
        for x in range(int(instruction[0])):
            container = stacks[start].pop()
            stacks[to].append(container)
    result = [stack.pop() for stack in stacks]  
    return ''.join(result)

if __name__ == "__main__":
    filename = argv[1]
    instructions, stacks = parse_data(filename)
    containers = get_top_containers(instructions, stacks)
    print(containers)