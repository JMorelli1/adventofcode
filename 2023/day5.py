import sys

input = open(sys.argv[1]).read().strip()
maps = input.split("\n\n")

seeds = maps[0].split(": ")[1]
seed_to_soil = maps[1].split(":\n")[1].split("\n")
soil_to_fertilizer = maps[2].split(":\n")[1].split("\n")
fertilizer_to_water = maps[3].split(":\n")[1].split("\n")
water_to_light = maps[4].split(":\n")[1].split("\n")
light_to_temperature = maps[5].split(":\n")[1].split("\n")
temperature_to_humidity = maps[6].split(":\n")[1].split("\n")
humidity_to_location = maps[7].split(":\n")[1].split("\n")

locations1 = []
locations2 = []
seed_pair = []

solution1 = 0
solution2 = 0


def run_maps(seed):
    soil_value = find_map_value(seed_to_soil, seed)
    fertilizer_value = find_map_value(soil_to_fertilizer, soil_value)
    water_value = find_map_value(fertilizer_to_water, fertilizer_value)
    light_value = find_map_value(water_to_light, water_value)
    temperature_value = find_map_value(light_to_temperature, light_value)
    humidity_value = find_map_value(temperature_to_humidity, temperature_value)
    location_value = find_map_value(humidity_to_location, humidity_value)

    return location_value


def run_maps_range(seed_range):
    soil_value = find_map_value_range(seed_to_soil, seed_range)
    fertilizer_value = find_map_value(soil_to_fertilizer, soil_value)
    water_value = find_map_value(fertilizer_to_water, fertilizer_value)
    light_value = find_map_value(water_to_light, water_value)
    temperature_value = find_map_value(light_to_temperature, light_value)
    humidity_value = find_map_value(temperature_to_humidity, temperature_value)
    location_value = find_map_value(humidity_to_location, humidity_value)

    return location_value


def find_map_value(map, source_value):
    dest = 0
    for map_set in map:
        destination_start, source_start, range_count = map_set.split(" ")
        if int(source_start) <= int(source_value) <= (int(source_start) + int(range_count)):
            dest = range(int(destination_start), (int(destination_start) + int(range_count)))[(int(source_value) - int(source_start))]

    if dest == 0:
        return source_value
    else:
        return dest


def find_map_value_range(map, seed_range):
    dest = 0
    for map_set in map:
        destination_start, source_start, range_count = map_set.split(" ")
        destination_start = int(destination_start)
        source_start = int(source_start)
        range_count = int(range_count)
        dest_range = range(destination_start, destination_start + range_count)

        if source_start <= seed_range[-1] <= (source_start + range_count):
            dest = dest_range[-1]
        elif seed_range[-1] < source_start:
            dest = seed_range[-1]

    return dest


for seed in seeds.split(" "):
    locations1.append(run_maps(seed))

# Generate seed source and seed range pairs
temp_pair = []
for sp in seeds.split(" "):
    temp_pair.append(int(sp))
    if len(temp_pair) == 2:
        seed_pair.append(temp_pair)
        temp_pair = []

for pair in seed_pair:
    locations2.append(run_maps_range(pair))


solution1 = locations1[0]
for location in locations1:
    if location < solution1:
        solution1 = location

solution2 = locations2[0]
for location in locations2:
    if location < solution2:
        solution2 = location

print(solution1)
print(solution2)
