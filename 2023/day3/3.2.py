from functools import reduce

# Specify the path to your file
file_path = "./input"

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]

def is_valid_char(char):
    return char.isdigit()

def join_rows(matrix):
    concatenated_rows = []
    for row in matrix:
        concatenated_rows += row
    return concatenated_rows

def main():
    gears = dict()

    matrix = read_input_file(file_path)
    total_sum = 0
    # Iterate through each line in the file
    for row in range(len(matrix)):
        # Iterate through each char in the line
        for col in range(len(matrix[0])):
            # check if current char is a number and the previous char is not a number
            if is_valid_char(matrix[row][col]) and (col - 1 < len(matrix[0]) and not is_valid_char(matrix[row][col - 1])):
                number = matrix[row][col]
                numbersize = 1
                # check if the next char is a number
                while col + numbersize < len(matrix[0]) and is_valid_char(matrix[row][col + numbersize]):
                    # add the next char to the number
                    number += matrix[row][col + numbersize]
                    numbersize += 1

                # found any surrounding *
                for rowSubset in range(row - 1 if row > 0 else 0 , row + 2 if row < len(matrix) - 1 else row + 1):
                    for colSubset in range(col - 1 if col > 0 else 0 , col + numbersize + 1 if col + numbersize < len(matrix[0]) else col + numbersize):
                        if matrix[rowSubset][colSubset] == '*':
                            # check if we have already seen this gear
                            if not (rowSubset, colSubset) in gears.keys():
                                # add the gear to the dict
                                gears.update({(rowSubset, colSubset) : []})
                            # add the number to the list surrounding number of the gear
                            gears[(rowSubset, colSubset)].append(number)

    # for each gear
    for gear in gears.keys():
        # check if the gear has 1 surrounding numbers
        if len(gears[gear]) == 2:
            # sum the product of the surrounding numbers
            total_sum += reduce(lambda a, b: int(a) * int(b), gears[gear])

    print(total_sum)

    
if __name__ == "__main__":
    main()