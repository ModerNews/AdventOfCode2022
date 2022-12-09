from data_fetcher import get_data


def populate_grid(size: int = 100):
    return [['.' for i in range(size)] for i in range(size)]


def extend_grid(grid: list[list[str]], by: int = 1):
    grid = [row + ['.' for i in range(by)] for row in grid]
    [grid.append(['.' for i in range(len(grid[0]))]) for j in range(by)]
    return grid

starting_position = [0, 0]
no_knots = 10

movement_grid = populate_grid(410)
movement_grid[0][0] = 'H'

mapping_grid = populate_grid(410)
mapping_grid[0][0] = 'T'

H = starting_position.copy()
T = {'0': H} | {f'{i + 1}': starting_position.copy() for i in range(0, no_knots)}

moves = [line.split(' ') for line in get_data(9, True).split('\n')[:-1]]

for move in moves:
    # Loops starts here to define 'ticks' - one tick equals to one step of head movement
    for i in range(int(move[1])):
        # Head movement
        movement_grid[H[1]][H[0]] = '.'
        if move[0] == 'R':
            H[0] += 1
        elif move[0] == 'L':
            H[0] += -1
        elif move[0] == 'U':
            H[1] += 1
        elif move[0] == 'D':
            H[1] += -1
        try:
            movement_grid[H[1]][H[0]] = 'H'
        except IndexError:
            movement_grid = extend_grid(movement_grid, 5)
            mapping_grid = extend_grid(mapping_grid, 5)
        finally:
            movement_grid[H[1]][H[0]] = 'H'


        # Tail movement
        for k, v in T.items():
            if k == '0':
                continue
            knot = T[k]
            diff = [T[f'{int(k) - 1}'][0] - knot[0], T[f'{int(k) - 1}'][1] - knot[1]]
            # movement along axis
            for axis in [0, 1]:  # It's just code optimization, `axis` represents 2d axis - 1 for y and 0 for x
                if abs(diff[axis]) == 2 and diff[1 - axis] == 0:
                    movement_grid[knot[1]][knot[0]] = '.'
                    knot[axis] += int(diff[axis] / 2)
                    movement_grid[knot[1]][knot[0]] = k
                    mapping_grid[knot[1]][knot[0]] = k if mapping_grid[knot[1]][knot[0]] != '10' else '10'

            for axis in ['x', 'y']:  # It's just code optimization, `axis` represents 2d axis
            # Diagonal movement
                if abs(diff[1 if axis == 'x' else 0]) >= 1 and abs(diff[0 if axis == 'x' else 1]) >= 2:
                    movement_grid[knot[1]][knot[0]] = '.'
                    knot[1] += int(diff[1] / (1 if axis == 'x' else 2))
                    knot[0] += int(diff[0] / (2 if axis == 'x' else 1))
                    movement_grid[knot[1]][knot[0]] = k
                    mapping_grid[knot[1]][knot[0]] = k if mapping_grid[knot[1]][knot[0]] != '10' else '10'
    if move == ['L', '5']:
        print('stop!')

movement_grid[0][0] = 's'
mapping_grid[T['10'][1]][T['10'][0]] = '10'


print('\n'.join([' '.join(row) for row in movement_grid]) + '\n')

print('\n'.join([' '.join(row) for row in mapping_grid]))

print('\n'.join([' '.join(row) for row in mapping_grid]).count('1'))
print(len(mapping_grid), len(movement_grid))