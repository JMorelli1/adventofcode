import sys
import regex

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

solution1 = 0
solution2 = 0

card_wins = []


# Recursive function to get all scratch cards
def count_total_cards(line_index):
    total = 0
    for wins in range(card_wins[line_index], 0, -1):
        if wins == 0:
            break
        else:
            total += count_total_cards(wins+line_index)
    return total + 1


for line in lines:
    winning_count = 0
    card_numbers, card_sets = line.split(": ")
    winning_numbers_set, card_set = card_sets.split(" | ")

    winning_numbers = regex.sub("\\s+(?=\\d)", "|", winning_numbers_set.strip()).split("|")
    card_values = regex.sub("\\s+(?=\\d+)", "|", card_set.strip()).split("|")

    for winning_number in winning_numbers:
        if winning_number in card_values:
            winning_count += 1

    if winning_count > 0:
        solution1 += pow(2, winning_count - 1)

    card_wins.append(winning_count)

for index, count in enumerate(card_wins):
    solution2 += count_total_cards(index)

print(solution1)
print(solution2)
