from data_fetcher import get_data

data = [[line[:int(len(line)/2)], line[int(len(line)/2):]] if line != '' else None for line in get_data(3).split('\n')][:-1]

print(data)
# Check if all rucksacks have been split evenly
assert all([len(rucksack[0]) == len(rucksack[1]) for rucksack in data])

# generates list of repeated items in rucksacks, this assumes that there can be more than one type of those,
# that's why for every rucksack there is set instead of singular entry
repeated_items: list[set] = [set([item for item in tuple(rucksack[0]) if item in rucksack[1]]) for rucksack in data]

# Calculates priorities based of ASCII value table
priorities = [[ord(item) - 96 if ord(item) > 96 else ord(item) - 64 + 26 for item in rucksack] for rucksack in repeated_items]
print(sum([sum(rucksack) for rucksack in priorities]))

# splitting into groups is done by finding first elf in group (every third in file) and then adding in second and third
groups = [[rucksack[0] + rucksack[1] for rucksack in data[leader_index*3:leader_index*3+3]] for leader_index in range(len(data[::3]))]  # Yeah, I did split those list to merge them now

badges = [[item for item in group[0] if (item in group[1] and item in group[2])][0] for group in groups]

# Calculates priorities based of ASCII value table, same as the first one,
# except this one assumes there can be only one badge, therefore only one priorrity per group
priorities = [[ord(item) - 96 if ord(item) > 96 else ord(item) - 64 + 26 for item in group][0] for group in badges]
print(sum(priorities))