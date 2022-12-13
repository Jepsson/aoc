import os

def get_moves(point, possible_moves, heightmap):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    for dir in dirs:
        x = point['pos'][0] + dir[0]
        y = point['pos'][1] + dir[1]
        if x >= 0 and x < len(heightmap[0]) and y >= 0 and y < len(heightmap):
            height = ord(heightmap[y][x])
            if height == ord('E'):
                if point['height'] == ord('z'):
                    possible_moves.append({'pos': (x,y),'height': height})
            elif height - point['height'] <= 1:
                possible_moves.append({'pos': (x,y),'height': height})

def check_moves(heightmap, start_pos: tuple,) -> dict:
    visited = set(start_pos)
    queue = [{'pos': start_pos, 'height': ord('a')}]
    distances = {}
    distances[start_pos] = 0

    while queue:
        possible_moves = []
        point = queue.pop(0)

        if point['pos'] in visited:
            continue

        visited.add(point['pos'])
        
        get_moves(point, possible_moves, heightmap)
        dist = distances[point['pos']] + 1
        for i in possible_moves:
            pos = i['pos']
            height = i['height']

            if pos not in distances or dist < distances[pos]:
                distances[pos] = dist
                queue.append({'pos': pos, 'height': height})
    
    return distances

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    heightmap = [line.rstrip('\n') for line in f]

    start_poses = []
    end_pos = (0,0)
    for i, s in enumerate(heightmap):
        if s.find('a') != -1:
            start_poses.append((s.find('a'), i))
        if s.find('E') != -1:
            end_pos = (s.find('E'), i)

    paths = [check_moves(heightmap, start_pos)[end_pos] for start_pos in start_poses]
    paths.sort()
    print(paths[0])
