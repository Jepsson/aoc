import os

lowered_case_offset = -96
upper_case_offset = -38

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    total_score = 0
    for l1 in f:
        l2 = next(f)
        l3 = next(f)

        for c in l1:
            if c in l2 and c in l3:
                badge = c
                break
            else:
                l1.replace(c, '')
                l2.replace(c, '')
                l3.replace(c, '')
    
        total_score += ord(badge) + (lowered_case_offset if badge.islower() else upper_case_offset)
  
    print(total_score)
