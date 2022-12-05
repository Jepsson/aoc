import os

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    count = 0
   
    for line in f:
        f = range(int(line.split('-')[0]), int(line.split('-')[1].split(',')[0])) 
        s = range(int(line.split('-')[1].split(',')[1]), int(line.split('-')[2]))
        fins = (s.start <= f.start <= s.stop) or (s.start <= f.stop <= s.stop)
        sins = (f.start <= s.start <= f.stop) or (f.start <= s.stop <= f.stop)
        count += 1 if fins or sins else 0
  
    print(count)
