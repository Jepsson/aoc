import os

signal_strength = {
    20: 0,
    60: 0,
    100: 0,
    140: 0,
    180: 0,
    220: 0
}

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    cycle = 0
    value = 1

    for line in f:
        for _ in range(2 if line.startswith('addx') else 1):
            cycle += 1
            signal_strength[cycle] = cycle * value if cycle in signal_strength.keys() else 0

        if line.startswith('addx'):
            value += int(line.split(' ')[1])

    print(sum(signal_strength.values()))
