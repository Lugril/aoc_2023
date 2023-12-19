def get_destination (destination, sources, reach, to_map):
    mapped = to_map.copy()
    for cnt in range(len(to_map)):
        for position in range(len(sources)):
            if to_map[cnt] >= sources[position] and to_map[cnt] < sources[position] + reach[position]:
                mapped[cnt] = (to_map[cnt] - sources[position]) + destination[position]
    return(mapped)

def convert_map(map):
    _, map = map.split(":\n")
    map = map.split("\n")
    for line in range(len(map)):
        map[line] = map[line].split(" ")
    return(map)

print("reading file")
input = open("input.txt", "r")
input = input.read()
print("splitting input")
almanac = input.split("\n\n")
seed_ranges = almanac.pop(0)

print("seeds seperatet from maps")
print("converting maps to lists")
for alma in range(len(almanac)):
    print("converting alma:", (almanac[alma]))
    almanac[alma]=convert_map(almanac[alma])

print("splitting seedranges")
_, seed_ranges = seed_ranges.split(": ")
print("splitting seedranges more")
seed_ranges = seed_ranges.split(" ")

tmp_result = 0
for seed in range (0,len(seed_ranges),2):
    seeds = []
    print("adding seedrage {}/{}".format(seed/2,len(seed_ranges)/2))
    print("{}-{}".format(seed_ranges[seed], seed_ranges[seed+1]))
    #print(seed_ranges[seed])
    for reach in range(int(seed_ranges[seed+1])):
        seeds.append(int(seed_ranges[seed])+reach)
    


#print("mappings:")
print("seedcount", len(seeds))
result = seeds.copy()
block = 0
for mapping in almanac:
    block += 1
    print(f"making progress: Block {block}/7")
    destination = []
    source = [] 
    reach = []
    for entry in mapping:
        destination.append(int(entry[0]))
        source.append(int(entry[1]))
        reach.append(int(entry[2]))
    result = get_destination(destination,source,reach,result)
    #print(result) 

#print(sorted(result))
print("nearest location:", sorted(result)[0])
    




