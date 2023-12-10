# Specify the path to your file
file_path = "./input.txt"

dic = {
    '|': ['UP', 'DOWN'],
    '-': ['LEFT', 'RIGHT'],
    'L': ['UP', 'RIGHT'],
    'J': ['UP', 'LEFT'],
    '7': ['DOWN', 'LEFT'],
    'F': ['DOWN', 'RIGHT'],
}

def start(map, neighbors):
    S = []
    if map[neighbors['UP']['y']][neighbors['UP']['x']] in '|7F':
        S.append('UP')
    if map[neighbors['DOWN']['y']][neighbors['DOWN']['x']] in '|LJ':
        S.append('DOWN')
    if map[neighbors['LEFT']['y']][neighbors['LEFT']['x']] in '-LF':
        S.append('LEFT')
    if map[neighbors['RIGHT']['y']][neighbors['RIGHT']['x']] in '-J7':
        S.append('RIGHT')
    for key, value in dic.items():
        if value == S:
            return key

def solve(input):
    map_data = [list(line) for line in input.split('\n')]
    y = next(i for i, line in enumerate(map_data) if 'S' in line)
    x = map_data[y].index('S')
    queue = [{'x': x, 'y': y, 'steps': 0}]
    visited = {(x, y)}
    max_steps = 0

    while queue:
        current = queue.pop(0)
        neighbors = {
            'UP': {'x': current['x'], 'y': current['y'] - 1, 'steps': current['steps'] + 1},
            'DOWN': {'x': current['x'], 'y': current['y'] + 1, 'steps': current['steps'] + 1},
            'LEFT': {'x': current['x'] - 1, 'y': current['y'], 'steps': current['steps'] + 1},
            'RIGHT': {'x': current['x'] + 1, 'y': current['y'], 'steps': current['steps'] + 1},
        }
        if map_data[current['y']][current['x']] == 'S':
            map_data[current['y']][current['x']] = start(map_data, neighbors)
        next_steps = [neighbors[dir] for dir in dic[map_data[current['y']][current['x']]]]
        next_steps = [step for step in next_steps if step['x'] >= 0 and step['y'] >= 0]
        next_steps = [step for step in next_steps if step['y'] < len(map_data) and step['x'] < len(map_data[0])]
        next_steps = [step for step in next_steps if (step['x'], step['y']) not in visited]
        visited.update((step['x'], step['y']) for step in next_steps)
        max_steps = max(max_steps, current['steps'])
        queue.extend(next_steps)

    return {'max': max_steps, 'map': map_data, 'visited': visited}

def main():
    with open(file_path, 'r') as f:
        input = f.read()
        print(solve(input)['max'])

if __name__ == "__main__":
    main()