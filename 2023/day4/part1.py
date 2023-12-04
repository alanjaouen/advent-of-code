# Specify the path to your file
file_path = "./input.txt"


def notEmptyString(s):
    return s != ""


def main():
    sum = 0
    # Open the file in 'r' mode (read mode)
    with open(file_path, "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Extract the first and last digits
            splited = line.replace("\n", "").split(":")[1].split("|")
            winingNumbers = set(filter(notEmptyString, splited[0].split(" ")))
            gameNumbers = set(filter(notEmptyString, splited[1].split(" ")))
            intersection = winingNumbers.intersection(gameNumbers)
            if len(intersection):
                sum += pow(2, len(intersection) - 1)

    print(sum)


if __name__ == "__main__":
    main()
