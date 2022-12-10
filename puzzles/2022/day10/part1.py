import os

signal_strength = {
    20: 0,
    60: 0,
    100: 0,
    140: 0,
    180: 0,
    220: 0
}

def update_signal_strenght(cycle, value):
    if cycle in signal_strength.keys():
        signal_strength[cycle] = cycle * value

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    cycle = 0
    value = 1

    for line in f:
        cycle += 1
        update_signal_strenght(cycle, value)

        if line.startswith('addx'):
            cycle += 1
            update_signal_strenght(cycle, value)
            value += int(line.split(' ')[1])

    print(sum(signal_strength.values()))
