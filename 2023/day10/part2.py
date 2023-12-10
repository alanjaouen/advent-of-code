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

def zoomin(map_data):
    big = []
    for yi in range(len(map_data)):
        line1 = []
        line2 = []
        line3 = []
        for xi in range(len(map_data[yi])):
            UP = '#' if 'UP' in dic[map_data[yi][xi]] else '.'
            DOWN = '#' if 'DOWN' in dic[map_data[yi][xi]] else '.'
            LEFT = '#' if 'LEFT' in dic[map_data[yi][xi]] else '.'
            RIGHT = '#' if 'RIGHT' in dic[map_data[yi][xi]] else '.'
            line1.extend(['.', UP, '.'])
            line2.extend([LEFT, map_data[yi][xi], RIGHT])
            line3.extend(['.', DOWN, '.'])
        big.extend([line1, line2, line3])
    return big

def zoomout(map_data):
    small = []
    for y in range(0, len(map_data), 3):
        line = [map_data[y + 1][x + 1] for x in range(0, len(map_data[y]), 3)]
        small.append(line)
    return small

def flood(map_data, x, y):
    visited = {(x, y)}
    queue = [{'x': x, 'y': y}]
    trapped = True
    while queue:
        current = queue.pop(0)
        neighbors = [
            {'x': current['x'], 'y': current['y'] - 1},
            {'x': current['x'], 'y': current['y'] + 1},
            {'x': current['x'] - 1, 'y': current['y']},
            {'x': current['x'] + 1, 'y': current['y']},
        ]
        next_steps = [neighbor for neighbor in neighbors if
                      0 <= neighbor['y'] < len(map_data) and 0 <= neighbor['x'] < len(map_data[0]) and
                      map_data[neighbor['y']][neighbor['x']] == '.' and
                      (neighbor['x'], neighbor['y']) not in visited]
        visited.update((step['x'], step['y']) for step in next_steps)
        queue.extend(next_steps)
        if not next_steps:
            trapped = False

    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if (x, y) in visited:
                map_data[y][x] = 'I' if trapped else 'O'

def main():
    with open(file_path, 'r') as f:
        input = f.read()
        result = solve(input)
        map_data = [[result['map'][y][x] if (x, y) in result['visited'] else '.' for x in range(len(result['map'][y]))] for y in range(len(result['map']))]
        big = zoomin(map_data)
        for y in range(len(big)):
            for x in range(len(big[y])):
                if big[y][x] == '.':
                    flood(big, x, y)
        small = zoomout(big)
        print(sum(row.count('I') for row in small))

if __name__ == "__main__":
    main()