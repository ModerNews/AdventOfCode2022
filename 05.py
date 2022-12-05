import re
from data_fetcher import get_data

crate_data_raw, moves = get_data(5, True).split('\n\n')

# Strip brackets, add dots as custom separator for full rows
crate_data = [line.replace('[', '').replace('] ', '.').replace(']', '') for line in crate_data_raw.split('\n')]
# Remove indexing row
crate_data[-1] = crate_data[-1][1:]

# Remove empty fields, add custom separators between them
# (if not added for two and more empty fields sum will start rounding - 9 is divisible by 3,
# and whole order will be displaced)
crate_data = [line.replace('    ', ' .').replace('   ', ' ') for line in crate_data]
print('\n'.join(crate_data))

max_length = len(crate_data[-1])

# Convert each row to list
crate_data = [crate_data[j] + ''.join([' ' for i in range(max_length - len(crate_data[j]))]) if len(crate_data[j]) < max_length else crate_data[j] for j in range(len(crate_data[:-1]))]
print('\n'.join(crate_data))

# Convert list of rows to list of columns, reverse them (so the highest item is last in list) and filter out empty spaces
crate_data_formatted = [list(reversed(list(filter(lambda x: x != ' ', [crate_data[i][j*2] for i in range(len(crate_data))])))) for j in range(len(crate_data[-1].split('.')))]

print(crate_data_formatted)

create_data_usage = crate_data_formatted.copy()
for move in moves.split('\n')[:-1]:
    data = [int(index) for index in re.findall(r'\d+', move)]
    for i in range(data[0]):
        temp = create_data_usage[data[1] - 1][-1]
        create_data_usage[data[1] - 1] = create_data_usage[data[1] - 1][:-1]
        create_data_usage[data[2] - 1].append(temp)

print(''.join([stack[-1] for stack in create_data_usage]))

create_data_usage = crate_data_formatted.copy()
for move in moves.split('\n')[:-1]:
    data = [int(index) for index in re.findall(r'\d+', move)]
    temp = create_data_usage[data[1] - 1][-data[0]:]
    create_data_usage[data[1] - 1] = create_data_usage[data[1] - 1][:-data[0]]
    create_data_usage[data[2] - 1] += temp

print(''.join([stack[-1] for stack in create_data_usage]))
