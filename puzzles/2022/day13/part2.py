import os
import ast

def comp(p1, p2):
    if isinstance(p1, list) and isinstance(p2, list):
        for pp1, pp2 in zip(p1,p2):
            ret = comp(pp1, pp2)
            if ret is not None:
                return ret
        return comp(len(p1), len(p2))
    elif isinstance(p1, list):
        return comp(p1, [p2])
    elif isinstance(p2, list):
        return comp([p1], p2)
    elif p1 < p2:
        return True
    elif p1 > p2:
        return False
    else:
        return None


with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    pairs = []
    for line in f:
        if line != '\n':
            pairs.append(ast.literal_eval(line))

    pos2 = 1
    pos6 = 2
    for i in range(int((len(pairs))/2)):
        p1 = pairs[i*2]
        p2 = pairs[i*2+1]
        if comp(p1, [[2]]):
            pos2 += 1
        if comp(p2, [[2]]):
            pos2 += 1
        if comp(p1, [[6]]):
            pos6 += 1
        if comp(p2, [[6]]):
            pos6 += 1

    print(pos2*pos6)
