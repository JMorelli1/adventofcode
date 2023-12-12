import sys
import regex

input = open(sys.argv[1]).read().strip()
maps = input.split("\n")

# Split, remove white space, and convert to int
race_times = [int(race_time) for race_time in regex.split("\\s+", maps[0].split(":")[1].strip())]
race_records = [int(race_record) for race_record in regex.split("\\s+", maps[1].split(":")[1].strip())]

race_time_full = int(regex.sub("\\s+", "", maps[0].split(":")[1].strip()))
race_record_full = int(regex.sub("\\s+", "", maps[1].split(":")[1].strip()))

solution1 = 1
solution2 = 1

options_count = []


def find_win_options(race_time, race_record):
    win_options = 0
    for race_second in range(race_time):
        if (race_time - race_second) * race_second > race_record:
            win_options += 1
    return win_options


for index, race_time in enumerate(race_times):
    options_count.append(find_win_options(race_time, race_records[index]))

for option in options_count:
    solution1 *= option

solution2 = find_win_options(race_time_full, race_record_full)

print(solution1)
print(solution2)
