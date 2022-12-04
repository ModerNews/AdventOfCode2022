from data_fetcher import get_data

pairs = [[[int(item) for item in elf.split('-')] for elf in line.split(',')] for line in get_data(4).split('\n')[:-1]]

print(pairs)
# Generates list of indexes for first assignee then checks them against all indexes of second assignee,
# Then does the same for second against the first, except for the same ones, as those where already counted in
overlaps = [all([index in range(pair[1][0], pair[1][1] + 1) for index in range(pair[0][0], pair[0][1] + 1)]) for pair in pairs] + \
           [all([index in range(pair[0][0], pair[0][1] + 1) for index in range(pair[1][0], pair[1][1] + 1)]) if range(pair[1][0], pair[1][1] + 1) != range(pair[0][0], pair[0][1] + 1) else False for pair in pairs]
print(overlaps)
print(sum(overlaps))

# Works similarly to the first one, except it reassigns value to the variable instead of generating whole in one step,
# thanks to that check was replaced to see if given pair was already counted in, as not only the same ones would be now counted twice
any_overlaps = [any([index in range(pair[1][0], pair[1][1] + 1) for index in range(pair[0][0], pair[0][1] + 1)]) for pair in pairs]
any_overlaps += [any([index in range(pair[0][0], pair[0][1] + 1) for index in range(pair[1][0], pair[1][1] + 1)]) if not any_overlaps[pairs.index(pair)] else False for pair in pairs]

print(any_overlaps)
print(sum(any_overlaps))