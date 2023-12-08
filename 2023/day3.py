import sys
import regex as re

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

all_lines_array = [[x for x in y] for y in lines]


# Scans to the left and right of number for continuous digits
def find_all_numbers(y, x):
    digit_locs = []
    for count in [0, 1, 2]:
        adjusted_x = x + count
        if 0 <= x + count < len(all_lines_array):
            if all_lines_array[y][adjusted_x].isdigit():
                if (y, adjusted_x) not in valid_numbers:
                    digit_locs.append((y, adjusted_x))
            else:
                break

    for count in [-1, -2]:
        adjusted_x = x + count
        if 0 <= x + count < len(all_lines_array):
            if all_lines_array[y][adjusted_x].isdigit():
                if (y, adjusted_x) not in valid_numbers:
                    digit_locs.append((y, adjusted_x))
            else:
                break

    if len(digit_locs) != 0:
        valid_numbers.extend(digit_locs)

    return digit_locs


# Sums value by using changes in the x and y coordinates
def calculate_values(digits):
    # Sort to have array in readable order
    digits.sort()

    prev_x = -1
    prev_y = -1
    value = ''
    values = []

    for y, x in digits:
        str_digit = all_lines_array[y][x]

        if prev_x != -1 and prev_y != -1 and (prev_x + 1 != x or prev_y != y):
            values.append(int(value))
            value = ''

        value += str_digit
        prev_x = x
        prev_y = y

    # Catch the final value generated
    values.append(int(value))
    return values


number_locations = []
symbol_locations = []
valid_numbers = list()

solution1 = 0
solution2 = 0

# Generates a tuple array of all symbol and number locations
for index, line in enumerate(lines):
    for index2, loc in enumerate(line):
        if loc.isdigit():
            number_locations.append((index, index2))
        if re.match('[^\\d|.]', loc) is not None:
            symbol_locations.append((index, index2))

# Scans around each symbol and adds found number tuples to valid_numbers
for line_index, value_index in symbol_locations:
    symbol_digit_locs = []

    for left_right in [-1, 0, 1]:
        for top_bottom in [-1, 0, 1]:
            adjusted_x = value_index + left_right
            adjusted_y = line_index + top_bottom
            if (adjusted_y, adjusted_x) in number_locations:
                digit_locs = find_all_numbers(adjusted_y, adjusted_x)
                symbol_digit_locs.extend(digit_locs)

    # Generate values surrounding symbols
    symbol_values = calculate_values(symbol_digit_locs)

    if len(symbol_values) == 2:
        solution2 += symbol_values[0] * symbol_values[1]

    for value in symbol_values:
        solution1 += value

    symbol_digit_locs.clear()

print(solution1)
print(solution2)
