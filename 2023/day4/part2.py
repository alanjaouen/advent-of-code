from functools import reduce

# Specify the path to your file
file_path = "./input.txt"


def notEmptyString(s):
    return s != ""


def main():
    cardMultiplier = {}
    with open(file_path, "r") as file:
        for line in file:
            cardNumber = int(
                list(filter(notEmptyString, line.split(":")[0].split(" ")))[1]
            )

            if not cardNumber in cardMultiplier.keys():
                cardMultiplier.update({cardNumber: 1})

            splited = line.replace("\n", "").split(":")[1].split("|")
            winingNumbers = set(filter(notEmptyString, splited[0].split(" ")))
            gameNumbers = set(filter(notEmptyString, splited[1].split(" ")))
            intersection = winingNumbers.intersection(gameNumbers)
            if len(intersection):
                for times in range(cardMultiplier.get(cardNumber)):
                    for i in range(len(intersection)):
                        cardMultiplier.update(
                            {
                                cardNumber
                                + i
                                + 1: cardMultiplier.get(cardNumber + i + 1, 1)
                                + 1
                            }
                        )

    print(reduce(lambda a, b: a + b, cardMultiplier.values()))


if __name__ == "__main__":
    main()
