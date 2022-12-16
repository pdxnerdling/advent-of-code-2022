from cmath import inf
from sys import argv

def print_grid(grid):
    for row in grid:
        print(row[490:510])

def get_grid(filename):
    file = open(filename, 'r')
    paths = []
    max_1 = 0
    for line in file:
        path = []
        split = line.replace("-> ", "").split()
        for pair in split:
            rock = pair.split(",")
            rock = [int(rock[0]), int(rock[1])]
            path.append(rock)
            if rock[1] > max_1:
                max_1 = rock[1]
        paths.append(path)
    midpoint = 500
    grid = [["." for _ in range(midpoint*2+1)] for _ in range(max_1+2)]
    grid[0][midpoint] = "+"
    for path in paths:
        for x in range(len(path)-1):
            if path[x][1] == path[x+1][1]:
                min1 = min(path[x][0], path[x+1][0])
                max1 = max(path[x][0], path[x+1][0])
                for r in range(max1-min1+1):     
                    grid[path[x][1]][min1+r-1] = "#"
            else:
                min2 = min(path[x][1], path[x+1][1])
                max2 = max(path[x][1], path[x+1][1])
                for l in range(max2-min2+1):
                    grid[min2+l][path[x][0]-1] = "#"
    grid.append(["#" for _ in range(midpoint*2+1)])
    #print_grid(grid)
    return grid, midpoint

def get_num_sand_grains(grid, start):
    go = True
    grain_count = 0
    while(go):
        air = True
        level = 0
        width = len(grid[0])
        one = start
        while(air):
            if grid[level+1][one] != "." and grid[level+1][one-1] != "." and grid[level+1][one+1] != ".":
                grid[level][one] = "o"
                grain_count += 1
                air = False
                if level == 0:
                    go = False
            elif grid[level+1][one] != "." and grid[level+1][one-1] == ".":
                one -= 1
            elif grid[level+1][one] != "." and grid[level+1][one+1] == ".":
                one +=1
            level += 1
    #print_grid(grid)
    return grain_count

if __name__ == "__main__":
    filename = argv[1]
    grid, start = get_grid(filename)
    num_grains = get_num_sand_grains(grid, start)
    print(num_grains)