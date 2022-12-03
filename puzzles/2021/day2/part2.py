import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    forward = 0
    depth = 0
    aim = 0
    for line in f:
        val = int(line.split(' ')[1])
        if line.startswith('forward'):
            forward += val
            depth += aim * val
        elif line.startswith('down'):
            aim += val
        elif line.startswith('up'):
            aim -= val

    print(forward * depth)
