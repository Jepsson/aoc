import os

crt = [['.']*40 for _ in range(6)]

def draw(cycle, sprite_pos: range):
    if cycle%40 in sprite_pos:
        crt[int(cycle/40)][cycle%40] = '#'

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    cycle = 0
    value = 1
    sprite_pos = range(0,3)

    for line in f:
        draw(cycle, sprite_pos)
        cycle += 1
        if line.startswith('addx'):
            draw(cycle, sprite_pos)
            cycle += 1
            value += int(line.split(' ')[1])
            sprite_pos = range(value-1, value+2)

    for r in crt:
        print(''.join(r))