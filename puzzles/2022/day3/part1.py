import os

lowered_case_offset = -96
upper_case_offset = -38

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    total_score = 0
    for line in f:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        
        for c in firstpart:
            if c in secondpart:
                not_unique_char = c
                break
            else:
                firstpart.replace(c, '')
                secondpart.replace(c, '')

        if not not_unique_char:
            not_unique_char = secondpart
        
        total_score += ord(not_unique_char) + (lowered_case_offset if not_unique_char.islower() else upper_case_offset)

    print(total_score)
