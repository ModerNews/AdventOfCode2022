from data_fetcher import get_data


def find_distinct_char_chain(string: str, length: int):
    for i in range(len(string)):
        if len(set(string[i:i+length])) == length:
            break
    return i + length


string = get_data(6)

print(find_distinct_char_chain(string, 4))
print(find_distinct_char_chain(string, 14))