import functools

# Specify the path to your file
file_path = "./input.txt"

def solve(time, distance):
    for i in range(distance // time, time + 1):
        if (time - i) * i > distance:
            return time - i * 2 + 1


def part2(input_str):
    lines = input_str.replace(' ', '').strip().split('\n')
    time = int(lines[0].split(':')[1])
    distance = int(lines[1].split(':')[1])
    return solve(time, distance)


def main():
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
        time = list(map(int, lines[0].split()[1:]))
        distance = list(map(int, lines[1].split()[1:]))
        races = [{'time': t, 'distance': d} for t, d in zip(time, distance)]
        options = [solve(race['time'], race['distance']) for race in races]
        result = functools.reduce(lambda a, b: a * b, options, 1)
        print(result)


if __name__ == "__main__":
    main()
