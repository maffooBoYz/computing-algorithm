#Game of Life
from random import randint
import tkinter as tk
original_grid = []
canvas_grid = []
y, x = 0, 0
# Offsets for all eight neighbours around a cell
poo = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]
alive = bool
while True:
    inpt = input("What size do you want game of life: ")
    try:
        inpt = abs(int(inpt))
    except:
        print("Enter a number...\n")
        continue
    all_cells = (inpt**2)
    for i in range(inpt):
        original_grid.append([])
    break
for i in range(all_cells):
    rando = randint(0, 1)
    if len(original_grid[y]) == inpt:
        y += 1
    original_grid[y].append(rando)

dimen = 250/len(original_grid)

root = tk.Tk()
root.title("Game of Life")

# Build the canvas grid once using the initial cell states
for y in range(len(original_grid)):
    canvas_grid.append([])
    for x in range(len(original_grid)):
        colour = "black" if original_grid[y][x] == 1 else "white"
        canvas = tk.Canvas(root, bg=colour, height=dimen, width=dimen)
        canvas.grid(column=x, row=y)
        canvas_grid[y].append(canvas)

def create_button():
    button = tk.Button(text="Click Me", command=solve, fg="red")
    button.grid(column=(inpt//2), row=inpt)
def solve():
    # Copy the current grid so we can compute the next generation
    new_grid = [row[:] for row in original_grid]

    for y in range(len(original_grid)):
        for x in range(len(original_grid)):
            alive = original_grid[y][x] == 1
            total = 0

            for dy, dx in poo:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(original_grid) and 0 <= nx < len(original_grid):
                    total += original_grid[ny][nx]

            if alive:
                if total != 2 and total != 3:
                    new_grid[y][x] = 0
            else:
                if total == 3:
                    new_grid[y][x] = 1

            colour = "black" if new_grid[y][x] == 1 else "white"
            canvas_grid[y][x].configure(bg=colour)

    # Update the original grid for the next iteration
    for y in range(len(original_grid)):
        for x in range(len(original_grid)):
            original_grid[y][x] = new_grid[y][x]

    create_button()

solve()
root.mainloop()
