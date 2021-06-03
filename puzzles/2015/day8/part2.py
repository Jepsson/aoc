import re

def main():
    literals = 0
    characters = 0
    with open("input") as fp:
        lines = fp.readlines()
        for line in lines:
            literals += len(line)
            line = re.sub('\\\\\\\\|\\\\"', 'aaaa', line)
            line = re.sub('\\\\x[0-9a-f][0-9a-f]', 'aaaaa', line)
            line = re.sub('\"', 'aaa', line)
            characters += len(line)
    
    print(f'literals: {literals}')
    print(f'characters: {characters}')
    print(f'characters - literals: {characters - literals}')
if __name__ == "__main__":
    main()