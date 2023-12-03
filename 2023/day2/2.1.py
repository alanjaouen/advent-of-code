import re

# Specify the path to your file
file_path = "./input"

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13

sum = 0
# Open the file in 'r' mode (read mode)
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # split line by char ;
        sets = line.split(";")
        is_valid = True
        for aset in sets:
            # split set by char
            colors = aset.split(",")
            for color in colors:
                result = re.search(r"\d+ (blue|red|green)", color).group(0)
                count = int(result.split(" ")[0])
                colorname = result.split(" ")[1]
                if (
                    (colorname == "blue" and count > MAX_BLUE)
                    or (colorname == "red" and count > MAX_RED)
                    or (colorname == "green" and count > MAX_GREEN)
                ):
                    is_valid = False
                    break

        if not is_valid:
            continue
        gameid = re.search(r"\d+", line).group(0)
        sum += int(gameid)

print(sum)
