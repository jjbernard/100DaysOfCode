# Fun with JSON data

import json
from pprint import pprint
from pathlib import Path
import os
from typing import Dict, List


def print_header():
    print('-------------------------------')
    print('      JSON ANALYSIS')
    print('-------------------------------')
    print()


def parse_file(datadir: str, filename: str) -> Dict:
    filepath = Path(os.path.dirname(__file__)) / datadir / filename

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def select_aquatic_mounts(data: dict) -> List:
    res = [
        mount['name'] for mount
        in data['mounts']['collected']
        if mount['isAquatic']
    ]

    return res


def select_aquatic_and_jumping_mounts(data: dict) -> List:
    res = [
        mount['name'] for mount
        in data['mounts']['collected']
        if mount['isAquatic'] and mount['isJumping']
    ]

    return res


def select_aquatic_and_jumping_and_flying_mounts(data: dict) -> List:
    res = [
        mount['name'] for mount
        in data['mounts']['collected']
        if mount['isAquatic'] and mount['isJumping'] and mount['isFlying']
    ]

    return res


def main():
    print_header()
    content = parse_file('data', 'mount-data.json')
    aquatic_and_jumping_and_flying = select_aquatic_and_jumping_and_flying_mounts(content)
    pprint(aquatic_and_jumping_and_flying)
    print(len(aquatic_and_jumping_and_flying))
    # should be zero ;-)


if __name__ == '__main__':
    main()
