import os


with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(map(int, list(line)))) 

    visible = 0
    for ri, r in enumerate(grid):
        if ri == 0 or ri == len(grid) - 1:
            visible += len(grid)
            continue

        for ci, c in enumerate(r):
            if ci == 0 or ci == len(r) - 1:
                visible += 1
                continue

            visible += 1 if all(tree[ci] < c for tree in grid[:ri]) or \
                all(tree[ci] < c for tree in grid[ri+1:]) or \
                all(tree < c for tree in grid[ri][:ci]) or \
                all(tree < c for tree in grid[ri][ci+1:]) else 0
    print(visible)
