import sys
import regex as re


def getint(num):
    if num == 'one':
        return '1'
    elif num == 'two':
        return '2'
    elif num == 'three':
        return '3'
    elif num == 'four':
        return '4'
    elif num == 'five':
        return '5'
    elif num == 'six':
        return '6'
    elif num == 'seven':
        return '7'
    elif num == 'eight':
        return '8'
    elif num == 'nine':
        return '9'
    return num


input = open(sys.argv[1]).read().strip()

solution1 = 0
solution2 = 0

for line in input.split('\n'):
    digits = re.findall('\\d', line)
    solution1 += int(digits[0] + digits[len(digits) - 1])

for line in input.split('\n'):
    stringDigits = re.findall('one|two|three|four|five|six|seven|eight|nine|\\d', line, overlapped=True)
    solution2 += int(getint(stringDigits[0]) + getint(stringDigits[len(stringDigits) - 1]))

print(solution1)
print(solution2)
