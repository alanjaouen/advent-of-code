# Specify the path to your file
file_path = "./input"


def read_input_file(file_path):
    with open(file_path, "r") as file:
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
    matrix = read_input_file(file_path)
    total_sum = 0
    # Iterate through each line in the file
    for row in range(len(matrix)):
        # Iterate through each char in the line
        for col in range(len(matrix[0])):
            # check if current char is a number and the previous char is not a number
            if is_valid_char(matrix[row][col]) and (
                col - 1 < len(matrix[0]) and not is_valid_char(matrix[row][col - 1])
            ):
                number = matrix[row][col]
                numbersize = 1
                # check if the next char is a number
                while col + numbersize < len(matrix[0]) and is_valid_char(
                    matrix[row][col + numbersize]
                ):
                    # add the next char to the number
                    number += matrix[row][col + numbersize]
                    numbersize += 1

                # get the subset of the matrix corresponding to the number and surrounding chars
                # subset of lines
                subset = matrix[
                    row - 1
                    if row > 0
                    else 0 : row + 2
                    if row < len(matrix) - 1
                    else row + 1
                ]
                # subset of columns
                for rowSubset in range(len(subset)):
                    subset[rowSubset] = subset[rowSubset][
                        col - 1
                        if col > 0
                        else 0 : col + numbersize + 1
                        if col + numbersize < len(matrix[0])
                        else col + numbersize
                    ]

                # get all chars in the subset, deduplicated
                charset = set(join_rows(subset))
                # remove all numbers and . from the charset
                charset = list(
                    filter(lambda x: not x.isdigit() and not x == ".", charset)
                )
                # if the charset is not empty, the number is surronunded by at least one symbol
                if len(charset) > 0:
                    total_sum += int(number)
    print(total_sum)


if __name__ == "__main__":
    main()
