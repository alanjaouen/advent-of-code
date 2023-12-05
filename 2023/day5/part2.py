from math import inf

# Specify the path to your file
file_path = "./input.txt"
# file_path = "./inputtest.txt"


def parse_map(file_path):
    maps = {}
    current_map = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("seeds:"):
                current_map = "seeds"
                maps[current_map] = list(map(int, line.split(":")[1].split()))
            elif line.startswith("seed-to-soil map:"):
                current_map = "seed_to_soil"
                maps[current_map] = []
            elif line.startswith("soil-to-fertilizer map:"):
                current_map = "soil_to_fertilizer"
                maps[current_map] = []
            elif line.startswith("fertilizer-to-water map:"):
                current_map = "fertilizer_to_water"
                maps[current_map] = []
            elif line.startswith("water-to-light map:"):
                current_map = "water_to_light"
                maps[current_map] = []
            elif line.startswith("light-to-temperature map:"):
                current_map = "light_to_temperature"
                maps[current_map] = []
            elif line.startswith("temperature-to-humidity map:"):
                current_map = "temperature_to_humidity"
                maps[current_map] = []
            elif line.startswith("humidity-to-location map:"):
                current_map = "humidity_to_location"
                maps[current_map] = []
            else:
                maps[current_map].append(list(map(int, line.split())))

    return maps


def input_to_output(map, input):
    for line in map:
        destinationRangeStart = line[0]
        sourceRangeStart = line[1]
        rangeLength = line[2]
        sourceRange = range(sourceRangeStart, sourceRangeStart + rangeLength)

        if not input in sourceRange:
            continue

        return destinationRangeStart + (input - sourceRangeStart)

    return input


def apply_mappings(result, input_data):
    current_input = input_data
    for key in result.keys():
        if key != "seeds":
            current_input = input_to_output(result[key], current_input)
    return current_input


def process_seed(seed, result, min_location):
    location = apply_mappings(result, seed)
    if location < min_location[0]:
        min_location[0] = location


def main():
    result = parse_map(file_path)

    min_location = inf
    i = 0
    while i < len(result.get("seeds")):
        for seed in range(
            result.get("seeds")[i], result.get("seeds")[i] + result.get("seeds")[i + 1]
        ):
            location = apply_mappings(result, seed)
            if location < min_location:
                min_location = location
                print(f"New min location: {min_location}")
        i += 2

    print(f"Min location: {min_location}")


if __name__ == "__main__":
    main()
