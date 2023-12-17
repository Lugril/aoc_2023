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
        #print("line", line)
        #print("line", map[line])
        map[line] = map[line].split(" ")
        #print("line", map[line])
    return(map)


input = open("input.txt", "r")
input = input.read()
almanac = input.split("\n\n")
seeds = almanac.pop(0)
#print(seeds)
#for x in almanac:
#    print(x)
for alma in range(len(almanac)):
    almanac[alma]=convert_map(almanac[alma])
#for x in almanac:
#    print(x)

_, seeds = seeds.split(": ")
seeds = seeds.split(" ")

#print("converted", convert_map(seed_soil))

print("mappings:")
#print(seeds)
result = []
for seed in seeds:
    result.append(int(seed))
print(result)
for mapping in almanac:
    #print(mapping)
    destination = []
    source = [] 
    reach = []
    for entry in mapping:
        destination.append(int(entry[0]))
        source.append(int(entry[1]))
        reach.append(int(entry[2]))
    #print("dest", destination)
    #print("src", source)
    #print("reach", reach)
    #print("conver", result)
    result = get_destination(destination,source,reach,result)
    print(result)

print(sorted(result))
print("nearest location:", sorted(result)[0])
    




