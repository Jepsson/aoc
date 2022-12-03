import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    incs = 0
    l1 = next(f)
    l2 = next(f)
    l3 = next(f)
    for l4 in f:
        sum1 = int(l1) + int(l2) + int(l3)
        sum2 = int(l2) + int(l3) + int(l4)

        incs += 1 if sum2 > sum1 else 0
        l1 = l2
        l2 = l3
        l3 = l4
    print(incs)
