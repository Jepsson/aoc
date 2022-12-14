import os
import turtle

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    scan = []
    x_range = None
    y_range = None
    paths = []
    for line in f:
        cords = line.strip().split(' -> ')
        for c in cords:
            x, y = map(int, c.split(','))
            paths.append((x,y))
            if not x_range:
                x_range = (x,x)
            elif x_range[0] > x:
                x_range = (x, x_range[1])
            elif x_range[1] < x:
                x_range = (x_range[0], x)
            if not y_range:
                y_range = (y,y)
            elif y_range[0] > y:
                y_range = (y, y_range[1])
            elif y_range[1] < y:
                y_range = (y_range[0], y)

    for i in range(y_range[1]-y_range[0]):
        print('.'*(x_range[1]-x_range[0]))
    print(paths)
    print(x_range)
    print(y_range)

    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Turtle")
    skk = turtle.Turtle()