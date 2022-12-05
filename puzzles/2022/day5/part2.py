import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    stacks_text = [next(f) for _ in range(8)]
    stacks_text.reverse()
    stacks = []
    for i in range(0,9):
        stacks.append([])

    for stack in stacks_text:
        for i in range(9):
            if stack[4*i+1] != ' ':
                stacks[i].append(stack[4*i+1])
    
    # throw away two lines
    next(f)
    next(f)

    for line in f:
        moves = int(line.split(' ')[1])
        move_from = int(line.split(' ')[3])-1
        move_to = int(line.split(' ')[5])-1

        for s in stacks[move_from][-moves:]:
            stacks[move_to].append(s)
            stacks[move_from].pop()

    ans = ""
    for s in stacks:
        ans += s.pop()
        
    print(ans)
