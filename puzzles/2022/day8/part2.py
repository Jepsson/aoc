import os


def trees_in_line(proposal, line):
    trees = 0
    for tree in line:
        trees += 1
        if tree >= proposal:
            break
    return trees

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    row_grid = []
    for line in f:
        line = line.strip()
        row_grid.append(list(map(int, list(line))))

    col_grid = list(map(list, zip(*row_grid)))
    scenic_score = 0
    for ri, r in enumerate(row_grid):
        for ci, c in enumerate(r):
            view = 1
            view *= trees_in_line(c, col_grid[ci][:ri][::-1])    #up
            view *= trees_in_line(c, col_grid[ci][ri+1:])        #down
            view *= trees_in_line(c, row_grid[ri][ci+1:])        #right
            view *= trees_in_line(c, row_grid[ri][:ci][::-1])    #left
            scenic_score = view if view > scenic_score else scenic_score 

    print(scenic_score)
