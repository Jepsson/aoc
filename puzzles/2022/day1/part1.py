import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    calories = []
    current_elf = 0
    for line in f:
        if(line == "\n"):
            calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    
    calories.sort(reverse=True)
    print(calories[0])
