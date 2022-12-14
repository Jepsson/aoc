import os


class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def update(self, val):
        self.min = min(val, self.min)
        self.max = max(val, self.max)

    def diff(self):
        return self.max - self.min


class Cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    scan = []
    x_range = Range(500, 500)
    y_range = Range(0, 0)
    paths = []
    for line in f:
        cords = line.strip().split(' -> ')
        path = []
        for c in cords:
            x, y = map(int, c.split(','))
            path.append(Cord(x, y))
            x_range.update(x)
            y_range.update(y)
        paths.append(path)

    for i in range(y_range.diff()+1):
        scan.append([])
        for j in range(x_range.diff()+1):
            scan[i].append('.')

    for path in paths:
        for i in range(len(path)-1):
            x1 = path[i].x - x_range.min
            x2 = path[i+1].x - x_range.min
            y1 = path[i].y - y_range.min
            y2 = path[i+1].y - y_range.min

            # x
            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2)):
                    scan[j][x1] = '#'
            # y
            if y1 == y2:
                for j in range(min(x1, x2), max(x1, x2)+1):
                    scan[y1][j] = '#'

    # start dropping sand
    s = Cord(500-x_range.min, 0-y_range.min)
    sand_units = 0
    while True:
        if s.y == y_range.max:
            print(f'Falling of the edge at {s.x}:{s.y}')
            break
        # d
        elif scan[s.y+1][s.x] == '.':
            s.y += 1
        # ld
        elif s.x != x_range.min and scan[s.y+1][s.x-1] == '.':
            s.y += 1
            s.x += -1
        # rd
        elif s.x != x_range.max and scan[s.y+1][s.x+1] == '.':
            s.y += 1
            s.x += 1
        # settle
        else:
            scan[s.y][s.x] = 's'
            s = Cord(500-x_range.min, 0-y_range.min)
            sand_units += 1

    for r in scan:
        print(''.join(r))
    print(sand_units)
