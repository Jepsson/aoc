import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    incs = 0
    l1 = next(f)
    for l2 in f:
        incs += 1 if int(l2) > int(l1) else 0
        l1 = l2
    print(incs)