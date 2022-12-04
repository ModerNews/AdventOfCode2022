from data_fetcher import get_data

max_elfs = sorted([sum([int(food) if food != '' else 0 for food in line.split('\n')]) for line in get_data(1).split('\n\n')], key=lambda x: -x)

print(max_elfs[0])
print(sum(max_elfs[0:3]))