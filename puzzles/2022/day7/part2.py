import os

class Node:
    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name

class File(Node):
    def __str__(self):
        return f' - {self.size} {self.name}\n'

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

class Dir(Node):
    def __str__(self):
        s = f'{self.name} {self.total_size} {True if self.total_size <= 100000 else False}\n'
        for c in self.children.values():
            if isinstance(c, File):
                s += f'{c.__str__()}'
        
        for c in self.children.values():
            if isinstance(c, Dir):
                s += f'{c.__str__()}'
        
        return s

    def __init__(self, name, parent):
        super().__init__(name)
        self.children = {}
        self.parent = parent
        self.total_size = 0

    def inc_size(self, size):
        self.total_size += size
        if self.parent:
            self.parent.inc_size(size)

    def add_dir(self, name, parent):
        self.children[name] = Dir(name, parent)

    def add_file(self, name, size):
        self.inc_size(size)
        self.children[name] = File(name, size)


with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    line = next(f)
    root = Dir('/', None)
    current_dir = root

    for line in f:
        line = line.strip()
        if line[0] == '$':
            command = line[2:].split(' ')
            if command[0] == 'cd':
                if command[1] == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.children[command[1]]
                    
        elif line.startswith('dir'):
            current_dir.add_dir(line.split(' ')[1], current_dir)
        else:
            size, name = line.split(' ')
            current_dir.add_file(name, int(size))

dirs = []
def find_small_enough(dir: Dir, size):
    if dir.total_size >= size:
        dirs.append(dir.total_size)
    
    for c in dir.children.values():
        if isinstance(c, Dir):
            find_small_enough(c, size)

unused = 70000000 - root.total_size
find_small_enough(root, 30000000 - unused)
dirs.sort()
print(dirs[0])
