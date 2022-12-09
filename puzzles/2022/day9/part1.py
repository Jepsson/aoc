import os

dirs = {
    'U': (0,  1),
    'D': (0, -1),
    'R': (1,  0),
    'L': (-1, 0)
}

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    knots = [[0,0] for _ in range(2)]
    t_positions = set()
    for line in f:
        dir = line[0]
        steps = int(line.split(' ')[1])

        for _ in range(steps):
            knots[-1] = list(map(sum, zip(knots[-1], dirs[dir])))
            for i in reversed(range(len(knots)-1)):
                x_dist = knots[i+1][0] - knots[i][0]
                y_dist = knots[i+1][1] - knots[i][1]
                if abs(x_dist) == 2 or abs(y_dist) == 2:
                    knots[i][0] += 1 if knots[i][0] < knots[i+1][0] else 0
                    knots[i][0] -= 1 if knots[i][0] > knots[i+1][0] else 0
                    knots[i][1] += 1 if knots[i][1] < knots[i+1][1] else 0
                    knots[i][1] -= 1 if knots[i][1] > knots[i+1][1] else 0                
                t_positions.add(tuple(knots[0]))
    
    print(len(t_positions))
