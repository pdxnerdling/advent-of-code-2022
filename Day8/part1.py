from sys import argv

def create_grid(filename):
    file = open(filename, 'r')
    data = file.read().splitlines()
    grid = []
    for line in data:
        grid.append(list(map(int, list(line))))
    return grid

def is_visible_from_north(grid, x, y):
    if x == 0:
        return True
    height = grid[x][y]
    for i in range(x):
        if grid[i][y] >= height:
            return False
    return True

def is_visible_from_south(grid, x, y):
    r_len = len(grid[0]) - 1
    if x == r_len:
        return True
    height = grid[x][y]
    for i in range(r_len - x):
        if grid[r_len - i][y] >= height:
            return False
    return True

def is_visible_from_west(grid, x, y):
    if y == 0:
        return True
    height = grid[x][y]
    for i in range(y):
        if grid[x][i] >= height:
            return False
    return True

def is_visible_from_east(grid, x, y):
    r_len = len(grid[0]) - 1
    if y == r_len:
        return True
    height = grid[x][y]
    for i in range(r_len - y):
        if grid[x][r_len - i] >= height:
            return False
    return True

def is_visible_from_road(grid, x, y):
    return (is_visible_from_east(grid, x, y) 
            or is_visible_from_west(grid, x, y)
            or is_visible_from_north(grid, x, y) 
            or is_visible_from_south(grid, x, y))

def get_visible_tree_count(grid):
    tc = 0
    row_len = len(grid[0])
    for x in range(row_len):
        for y in range(row_len):
            if is_visible_from_road(grid, x, y):
                tc += 1
    return tc

if __name__ == "__main__":
    filename = argv[1]
    grid = create_grid(filename)
    visible_tree_count = get_visible_tree_count(grid)
    print(visible_tree_count)