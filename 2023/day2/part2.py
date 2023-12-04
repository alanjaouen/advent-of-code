import re

# Specify the path to your file
file_path = "./input"

sum = 0
# Open the file in 'r' mode (read mode)
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # split line by char ;
        sets = line.split(";")
        # count minimum of each color
        min_red, min_blue, min_green = 0, 0, 0
        for aset in sets:
            # split set by char
            colors = aset.split(",")
            for color in colors:
                result = re.search(r"\d+ (blue|red|green)", color).group(0)
                count = int(result.split(" ")[0])
                colorname = result.split(" ")[1]
                print("color " + colorname + " count " + str(count))
                if colorname == "blue" and count > min_blue:
                    min_blue = count
                elif colorname == "red" and count > min_red:
                    min_red = count
                elif colorname == "green" and count > min_green:
                    min_green = count

        gamepower = min_blue * min_red * min_green
        sum += int(gamepower)

print(sum)
