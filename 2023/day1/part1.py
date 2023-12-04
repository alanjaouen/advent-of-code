# Specify the path to your file
file_path = "./input"

sum = 0
# Open the file in 'r' mode (read mode)
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Extract the first and last digits
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        sum += int(first_digit + last_digit)

print(sum)
