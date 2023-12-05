import math

# Specify the path to your file
file_path = "./input.txt"


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


def main():
    min = math.inf
    result = parse_map(file_path)

    for seed in result.get("seeds"):
        soil = input_to_output(result.get("seed_to_soil"), seed)
        fertilizer = input_to_output(result.get("soil_to_fertilizer"), soil)
        water = input_to_output(result.get("fertilizer_to_water"), fertilizer)
        light = input_to_output(result.get("water_to_light"), water)
        temperature = input_to_output(result.get("light_to_temperature"), light)
        humidity = input_to_output(result.get("temperature_to_humidity"), temperature)
        location = input_to_output(result.get("humidity_to_location"), humidity)
        # print(f"Seed {seed} is in soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")
        if location < min:
            min = location

    print(f"Min location: {min}")


if __name__ == "__main__":
    main()
