import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(grid):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while grid[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    grid[r][c] = 2

def get_current_state(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return "WON"
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return "NOT OVER"
    for i in range(3):
        for j in range(3):
            if (grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]):
                return "NOT OVER"
    for j in range(3):
        if grid[3][j] == grid[3][j+1]:
            return "NOT OVER"
    for i in range(3):
        if grid[i][3] == grid[i+1][3]:
            return "NOT OVER"
    return "LOST"
    
def move_up(grid):
    #Implement This Function
    grid = transpose(grid)
    grid, hasChanged = move_left(grid)
    grid = transpose(grid)
    return grid, hasChanged

def move_down(grid):
    #Implement This Function
    grid = transpose(grid)
    grid, hasChanged = move_right(grid)
    grid = transpose(grid)
    return grid, hasChanged

def move_right(grid):
    #Implement This Function
    grid = reverse(grid)
    grid,hasChanged = move_left(grid)
    grid = reverse(grid)
    return grid,hasChanged

def move_left(grid):
    #Implement This Function
    grid,hasChanged1 = compress(grid)
    grid,hasChanged2 = merge(grid)
    hasChanged = hasChanged1 or hasChanged2
    grid,tempChange = compress(grid)
    return grid, hasChanged

def compress(grid):
    new_grid = []
    hasChanged = False
    for i in range(4):
        new_grid.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if j != pos:
                    hasChanged = True
                pos+=1
    return new_grid, hasChanged

def merge(grid):
    hasChanged = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0
                hasChanged = True
    return grid, hasChanged

def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][4 - j - 1])
    return new_grid

def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i])
    return new_grid