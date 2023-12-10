# Specify the path to your file
file_path = "./input.txt"

def get_hand_type(hand):
    while 1 in hand:
        hand = [
            option if card == 1 else card
            for card in hand
            for option in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        ]
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    counts_array = list(counts.values())
    if 5 in counts_array:
        return 6
    if 4 in counts_array:
        return 5
    if 3 in counts_array and 2 in counts_array:
        return 4
    if 3 in counts_array:
        return 3
    if counts_array.count(2) == 2:
        return 2
    if 2 in counts_array:
        return 1
    return 0



def compare(a, b):
    hand_type_a = get_hand_type(a)
    hand_type_b = get_hand_type(b)
    if hand_type_a != hand_type_b:
        return hand_type_a - hand_type_b
    return sum(a[i] - b[i] for i in range(len(a)))


def card_number(card, jokers):
    if card == 'T':
        return 10
    if card == 'J':
        return 1 if jokers else 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14
    return int(card)

def main():
    jokers = True
    with open(file_path, 'r') as f:
        input_str = f.read()
        lines = input_str.strip().split('\n')
        hands = [
            {
                'bid': int(line.split(' ')[1]),
                'hand': [card_number(card, jokers) for card in line.split(' ')[0]],
            }
            for line in lines
        ]
        hands.sort(key=lambda x: compare(x['hand'], x['hand']))
        result =  sum(hand['bid'] * (index + 1) for index, hand in enumerate(hands))
        print(result)

if __name__ == "__main__":
    main()
