import os

rules_points = {
    'A': {'X': 3, 'Y': 6, 'Z': 0}, # rock
    'B': {'X': 0, 'Y': 3, 'Z': 6}, # paper
    'C': {'X': 6, 'Y': 0, 'Z': 3}  # scissors
}

shape_points = {
    'X': 1, # rock
    'Y': 2,  # paper
    'Z': 3   # scissors
}

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:


    total_score = 0
    for line in f:
        opponent = line[0]
        me = line[2]

        total_score += shape_points[me]
        total_score += rules_points[opponent][me]
        
    print(total_score)
