import functools
import re

# Specify the path to your file
file_path = "./input.txt"

def parse(input):
    steps, maps_str = input.split('\n\n')
    maps = {}
    for line in maps_str.split('\n'):
        key, L, R = re.match(r'^(.+) = \((.+), (.+)\)$', line).groups()
        maps[key] = {'L': L, 'R': R}
    return steps, maps

def walk(key, steps, maps, dest=lambda key: key == 'ZZZ'):
    count = 0
    while not dest(key):
        for step in steps:
            key = maps[key][step]
        count += 1
    return count * len(steps)

def main():
    with open(file_path, 'r') as f:
        input = f.read()
        steps, maps = parse(input)
        print(walk('AAA', steps, maps))

if __name__ == "__main__":
    main()