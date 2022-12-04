import requests
import os
from dotenv import load_dotenv

# session cookie can be specified in .env file, if None is available, or internet connection is not working it will read cached file instead
load_dotenv()

__all__ = ['get_data']


def get_data(day: int):
    path = f'cache/{day}_input.txt'
    cookies = {'session': os.getenv('ADVENT_SESSION', None)}
    if cookies['session']:
        try:
            with requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies=cookies) as response:
                data = response.text
            with open(path, 'w+') as file:
                file.write(data)
            return data
        except requests.exceptions.RequestException:  # Catches base requests library exception and defaults to cached data
            pass

    if os.path.exists(path):
        with open(path, 'r+') as file:
            data = file.read()
            return data
    else:
        raise FileNotFoundError('There is no data cached for this day')