import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    text = next(f)
    for i in range(len(text)):
        if len(set(text[i:i+14])) == 14:
            print(i+14)
            break
