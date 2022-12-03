import os

moves = {
    #    lose       draw       win
    'A': {'X': 'Z', 'Y':  'X', 'Z': 'Y'}, # rock
    'B': {'X': 'X', 'Y':  'Y', 'Z': 'Z'}, # paper
    'C': {'X': 'Y', 'Y':  'Z', 'Z': 'X'}  # scissors
}

rules_points = {
    #    rock    paper   scissors
    'A': {'X': 3, 'Y': 6, 'Z': 0}, # rock
    'B': {'X': 0, 'Y': 3, 'Z': 6}, # paper
    'C': {'X': 6, 'Y': 0, 'Z': 3}  # scissors
}

shape_points = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3  # scissors
}

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:


    total_score = 0
    for line in f: 
        opponent = line[0]
        me = line[2]

        total_score += rules_points[opponent][moves[opponent][me]]
        total_score += shape_points[moves[opponent][me]]
        
    print(total_score)
