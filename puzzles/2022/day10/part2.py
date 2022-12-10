import os

crt = [['.']*40 for _ in range(6)]
with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    cycle = 0
    value = 1

    for line in f:
        for _ in range(2 if line.startswith('addx') else 1):
            crt[int(cycle/40)][cycle%40] = '#' if cycle%40 in range(value-1, value+2) else '.'
            cycle += 1
        
        if line.startswith('addx'):
            value += int(line.split(' ')[1])

    for r in crt:
        print(''.join(r))
