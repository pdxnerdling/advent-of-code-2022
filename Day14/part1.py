from cmath import inf
from sys import argv

START = [500, 0]

def print_grid(grid):
    for row in grid:
        print(row)

def get_grid(filename):
    file = open(filename, 'r')
    paths = []
    max_0 = 500
    max_1 = 0
    min_0 = 500
    for line in file:
        path = []
        split = line.replace("-> ", "").split()
        for pair in split:
            rock = pair.split(",")
            rock = [int(rock[0]), int(rock[1])]
            path.append(rock)
            if rock[0] > max_0:
                max_0 = rock[0]
            if rock[0] < min_0:
                min_0 = rock[0]
            if rock[1] > max_1:
                max_1 = rock[1]
        paths.append(path)
    dif_0 = max_0 - min_0 + 1
    grid = [["." for _ in range(dif_0+1)] for _ in range(max_1+1)]
    grid[0][500-min_0+1] = "+"
    for path in paths:
        for x in range(len(path)-1):
            if path[x][1] == path[x+1][1]:
                min1 = min(path[x][0], path[x+1][0])
                max1 = max(path[x][0], path[x+1][0])
                for r in range(max1-min1+1):     
                    grid[path[x][1]][min1-max_0+r-1] = "#"
            else:
                min2 = min(path[x][1], path[x+1][1])
                max2 = max(path[x][1], path[x+1][1])
                for l in range(max2-min2+1):
                    grid[min2+l][path[x][0]-max_0-1] = "#"
    print_grid(grid)
    return grid, 500-min_0+1

def get_num_sand_grains(grid, start):
    go = True
    i = 1
    height = len(grid)
    width = len(grid[0])
    grain_count = 0
    while(go):
        air = True
        level = 0
        one = start
        while(air):
            if one == width-1 or one-1 == 0 or level+2 > height:
                air = False
                go = False
            elif grid[level+1][one] != "." and grid[level+1][one-1] != "." and grid[level+1][one+1] != ".":
                grid[level][one] = "o"
                grain_count += 1
                air = False
            elif grid[level+1][one] != "." and grid[level+1][one-1] == ".":
                one -= 1
                if one == 0:
                    print(one)
                    print("exit left")
                    air = False
                    go = False
            elif grid[level+1][one] != "." and grid[level+1][one+1] == ".":
                one +=1
                if one == width:
                    print(one)
                    print("exit right")
                    air = False
                    go = False
            level += 1
    return grain_count
    


if __name__ == "__main__":
    filename = argv[1]
    grid, start = get_grid(filename)
    num_grains = get_num_sand_grains(grid, start)
    print(num_grains)