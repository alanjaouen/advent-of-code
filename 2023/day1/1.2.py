import re

# Specify the path to your file
file_path = "./input"


def convertchar(char):
    if char == "one":
        return "1"
    elif char == "two":
        return "2"
    elif char == "three":
        return "3"
    elif char == "four":
        return "4"
    elif char == "five":
        return "5"
    elif char == "six":
        return "6"
    elif char == "seven":
        return "7"
    elif char == "eight":
        return "8"
    elif char == "nine":
        return "9"
    else:
        return char


def extract_digits(line):
    # Extract all digits or spelled-out numbers using regex
    numbers = "one|two|three|four|five|six|seven|eight|nine"

    # Get the first and last digit or spelled-out number
    first_digit = convertchar(re.search(r"\d|" + numbers, line).group(0))
    last_digit = convertchar(re.findall(r"\d|" + numbers[::-1], line[::-1])[0][::-1])
    return first_digit, last_digit


sum = 0
# Open the file in 'r' mode (read mode)
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Extract the first and last digits
        first_digit, last_digit = extract_digits(line)
        sum += int(first_digit + last_digit)

print(sum)
