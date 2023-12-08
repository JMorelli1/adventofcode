import sys
import regex as re

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")

cube_sets = {
    "green": 13,
    "red": 12,
    "blue": 14
}

cube_mins = {
    "green": 0,
    "red": 0,
    "blue": 0
}

def ispossible(cubes):
    possible = True
    for cube in cubes.split(', '):
        total, color = cube.split(' ')
        if int(total) > cube_sets[color]:
            possible = False
    return possible


def getmins(cubes):
    for cube in cubes.split(', '):
        total, color = cube.split(' ')
        total_int = int(total)
        if total_int > cube_mins[color]:
            cube_mins[color] = total_int


solution1 = 0
solution2 = 0

for line in lines:
    number, game = line.split(': ')
    game_number = re.search('\\d+', number).group()
    possible = True
    cube_mins = {
        "green": 0,
        "red": 0,
        "blue": 0
    }

    for sets in game.split('; '):
        if not ispossible(sets):
            possible = False
        getmins(sets)

    if possible:
        solution1 += int(game_number)

    solution2 += cube_mins['green'] * cube_mins['red'] * cube_mins['blue']

print(solution1)
print(solution2)
