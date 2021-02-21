"""
Aim: Look at a 5x5 (can be larger or smaller) board and determine which cells are alive or dead after updating them
Rules:
    - If an alive cell is surrounded by (2 or 3) living cells, it will survive
    - Otherwise it dies
    - A dead cell becomes alive if it is surrounded by 3 living cells
## 0 = Dead cell
## 1 = Live cell
## dead_or_alive - True = alive, False = dead
To determine if the current cell is dead we will either have a True or a False value for dead_or_alive
"""
total = int
dead_or_alive = bool
y, x = 0, 0
"""----------------------------------------------------------------------------------------------"""
grid = [[0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1]]
new_grid = []
for i in range(len(grid)):
    new_grid.append([])
for i in range(len(grid)**2):
    if len(new_grid[y]) == 5:
        y += 1
        x = 0
    new_grid[y].append(grid[y][x])
    x += 1
for i in new_grid:
    print(i)
"""----------------------------------------------------------------------------------------------"""
def middle(y, x):
    total = 0
    x -= 1
    y -= 1
    for i in range(2):
        total += grid[y][x]
        x += 1
    for i in range(2):
        total += grid[y][x]
        y += 1
    for i in range(2):
        total += grid[y][x]
        x -= 1
    total += grid[y][x]
    y -= 1
    total += grid[y][x]
    x += 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def top_right(y, x):
    total = 0
    x -= 1
    total += grid[y][x]
    y += 1
    total += grid[y][x]
    x += 1
    total += grid[y][x]
    y -= 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    if dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def top_left(y, x):
    total = 0
    x += 1
    total += grid[y][x]
    y += 1
    total += grid[y][x]
    x -= 1
    total += grid[y][x]
    y -= 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def bottom_left(y, x):
    total = 0
    x += 1
    total += grid[y][x]
    y -= 1
    total += grid[y][x]
    x -= 1
    total += grid[y][x]
    y += 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def bottom_right(y, x):
    total = 0
    x -= 1
    total += grid[y][x]
    y -= 1
    total += grid[y][x]
    x += 1
    total += grid[y][x]
    y += 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def top_edge(y, x):
    total = 0
    x -= 1
    total += grid[y][x]
    y += 1
    total += grid[y][x]
    for _ in range(2):
        x += 1
        total += grid[y][x]
        
    y -= 1
    total += grid[y][x]
    x -= 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def bottom_edge(y, x):
    total = 0
    x += 1
    total += grid[y][x]
    y -= 1
    total += grid[y][x]
    for i in range(2):
        x -= 1
        total += grid[y][x]
    y += 1
    total += grid[y][x]
    x += 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    else:
        if total >= 3:
            new_grid[y][x] = 1
def left_edge(y, x):
    total = 0
    y -= 1
    total += grid[y][x]
    x += 1
    total += grid[y][x]
    for _ in range(2):
        y += 1
        total += grid[y][x]
    x -= 1
    total += grid[y][x]
    y -= 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
def right_edge(y, x):
    total = 0
    y -= 1
    total += grid[y][x]
    x -= 1
    total += grid[y][x]
    for _ in range(2):
        y += 1
        total += grid[y][x]
    x += 1
    total += grid[y][x]
    y -= 1
    if dead_or_alive == True:
        if total != 2 and total != 3:
            new_grid[y][x] = 0
    elif dead_or_alive == False:
        if total >= 3:
            new_grid[y][x] = 1
"""----------------------------------------------------------------------------------------------"""
y, x = 0, 0
for i in range((len(grid[0])**2)):
    if y > 4:
        y = 0
        x += 1
    if grid[y][x] == 1:
        dead_or_alive = True
    else:
        dead_or_alive = False
    if (x != 0 and y !=0) and (x != (len(grid) -1) and y != (len(grid) -1)):
        middle(y, x)
    if (y == 0) and (x == 0):
        top_left(y, x)
    if (y == (len(grid) -1)) and (x == 0):
        bottom_left(y, x)
    if (y == 0) and (x == (len(grid) -1)):
        top_right(y, x)
    if y == ((len(grid) -1)) and (x == (len(grid) -1)):
        bottom_right(y, x)
    if y == 0 and (x != 0 and x != (len(grid) -1)):
        top_edge(y, x)
    if y == (len(grid) -1) and (x != 0 and x != (len(grid) -1)):
        bottom_edge(y, x)
    if x == 0 and (y != 0 and y != (len(grid) -1)):
        left_edge(y, x)
    if x == (len(grid) -1) and (y != 0 and y != (len(grid) -1)):
        right_edge(y, x)
    y += 1
"""----------------------------------------------------------------------------------------------"""
print("\n")
for i in new_grid:
    print(i)
