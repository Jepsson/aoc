import os
import re
import operator
import math

ops = {
    '+': operator.add,
    '*': operator.mul
}

def op(old: int, op_func: operator, op_val: int) -> int:
    return op_func(old, op_val)

with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as f:
    monkeys = []
    inspections = []

    for line in f:
        if line.startswith('Monkey'):
            inspections.append(0)
            items = list(map(int, re.findall('[0-9]+', next(f))))

            line = next(f).split(' ')
            op_func = line[6]
            try:
                op_val = int(line[7])
            except:
                op_val = None
            test = int(next(f).split(' ')[5])
            true = int(next(f).split(' ')[9])
            false = int(next(f).split(' ')[9])
            monkeys.append({
                'items': items,
                'op_func': ops[op_func],
                'op_val': op_val,
                'div': test,
                'true': true,
                'false': false})
    
    lcm = math.lcm(*[m['div'] for m in monkeys])
    for i in range(10000):
        for m, monkey in enumerate(monkeys):
            for item in monkey['items']:
                inspections[m] += 1
                item = op(item, monkey['op_func'], monkey['op_val'] if monkey['op_val'] != None else item)
                item = item % lcm
                if item % monkey['div'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)
            monkey['items'] = []
    
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])
