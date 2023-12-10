# Specify the path to your file
file_path = "./input.txt"

def solve(time, distance):
    for i in range(distance // time, time + 1):
        if (time - i) * i > distance:
            return time - i * 2 + 1

def main():
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
        time = int(lines[0].split(':')[1])
        distance = int(lines[1].split(':')[1])
        result = solve(time, distance)
        print(result)


if __name__ == "__main__":
    main()
