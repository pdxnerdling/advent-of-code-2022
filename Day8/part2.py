from sys import argv

def create_grid(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    grid = []
    for line in data:
        grid.append(list(map(int, list(line))))
    return grid

def scenic_count_west(grid, x, y):
    height = grid[x][y]
    count = 0
    if y == 0:
        return 0
    for i in range(y):
        count += 1
        if grid[x][y-i-1] >= height:
            return count
    return count

def scenic_count_east(grid, x, y):
    g_len = len(grid[0])
    height = grid[x][y]
    count = 0
    if y == g_len:
        return count
    for i in range(1, g_len-y):
        count += 1
        if grid[x][y+i] >= height:
            return count
    return count

def scenic_count_south(grid, x, y):
    g_len = len(grid[0])
    height = grid[x][y]
    count = 0
    if x == g_len:
        return count
    for i in range(1, g_len-x):
        count += 1
        if grid[x+i][y] >= height:
            return count
    return count

def scenic_count_north(grid, x, y):
    height = grid[x][y]
    count = 0
    if x == 0:
        return 0
    for i in range(x):
        count += 1
        if grid[x-i-1][y] >= height:
            return count
    return count

def calculate_tree_scenic_score(grid, x, y):
    return (scenic_count_west(grid, x, y)
            * scenic_count_east(grid, x, y) 
            * scenic_count_north(grid, x, y)
            * scenic_count_south(grid, x, y))

def calculate_highest_scenic_score(grid):
    grid_len = len(grid[0])
    highest = 0
    for x in range(grid_len):
        for y in range(grid_len):
            scenic_score = calculate_tree_scenic_score(grid, x, y)
            if highest <= scenic_score:
                highest = scenic_score
    return highest

if __name__ == "__main__":
    filename = argv[1]
    grid = create_grid(filename)
    highest_scenic_score = calculate_highest_scenic_score(grid)
    print(highest_scenic_score)