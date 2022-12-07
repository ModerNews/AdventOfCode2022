import os

from data_fetcher import get_data

max_size = 100000
total_space = 70000000
needed_space = 30000000

def execute_command(commands: list[list], workdir: dict):
    # while len(commands) != 0:

    command = commands[0]
    commands.pop(0)
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                return
            else:
                if command[2] not in workdir.keys():
                    workdir[command[2]] = {}
                execute_command(commands, workdir[command[2]])
        elif command[1] == 'ls':
            pass
    else:
        if command[0] == 'dir':
            workdir[command[1]] = {}
        else:
            workdir[command[1]] = int(command[0])
    if len(commands) != 0:
        if commands[0][1] == 'cd':
            if commands[0][2] == '..':
                commands.pop(0)
                return
    if len(commands) != 0:
        execute_command(commands, workdir)
    return


def calculate_directory_size(dir: dict):
    is_file = {k: isinstance(v, int) for k, v in dir.items()}
    assert all(is_file)
    return int(sum(dir.values()))


def calculate_total_size(dir: dict, directory_sizes: list):
    sum = 0
    for k, v in dir.items():
        if isinstance(dir[k], dict):
            temp = calculate_total_size(dir[k], directory_sizes)
            # print(dir[k],'\n\t', temp)
            directory_sizes.append(temp)
            dir[k] = temp
            sum += temp
        elif isinstance(dir[k], int):
            sum += dir[k]
    else:

        return sum


if __name__ == '__main__':
    dir_tree = {}
    data = [line.split(' ') for line in get_data(7)[:-1].split('\n')]
    execute_command(data, dir_tree)

    print(dir_tree)

    directory_sizes = []
    calculate_total_size(dir_tree, directory_sizes)
    print(dir_tree)
    print(sum([v for v in directory_sizes if v <= max_size]))
    dir_spaces = sorted(directory_sizes)
    needed_space = needed_space - (total_space - directory_sizes[-1])
    print(min([space for space in dir_spaces if space > needed_space]))
