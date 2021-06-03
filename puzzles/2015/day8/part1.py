import re

def main():
    literals = 0
    characters = 0
    with open("input") as fp:
        lines = fp.readlines()
        for line in lines:
            literals += len(line)
            line = re.sub('\\\\\\\\|\\\\"|\\\\x[0-9a-f][0-9a-f]', 'a', line)
            line = re.sub('\"', '', line)
            characters += len(line)
    
    print(f'literals: {literals}')
    print(f'characters: {characters}')
    print(f'literals - characters: {literals - characters}')
if __name__ == "__main__":
    main()