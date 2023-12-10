# Specify the path to your file
file_path = "./input.txt"

def solve(input, fn):
    sequences = [list(map(int, line.split(' '))) for line in input.split('\n')]
    histories = [calculate_history(sequence) for sequence in sequences]
    return sum(map(fn, histories))

def calculate_history(sequence):
    history = [sequence]
    differences = sequence
    while any(x != 0 for x in differences):
        differences = [curr - sequence[i - 1] for i, curr in enumerate(differences)]
        history.append(differences)
    return history

def get_prev_number(history):
    for i in range(len(history) - 2, -1, -1):
        history[i].append(history[i][-1] + history[i + 1][-1])
    return history[0][-1]

def main():
    with open(file_path, 'r') as f:
        input = f.read()
        print(solve(input, get_prev_number))

if __name__ == "__main__":
    main()