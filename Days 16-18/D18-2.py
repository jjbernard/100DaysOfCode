# Todo: when .py file found parse it to return import statements
# Todo: update a global dict (or class?) with import statements and counter

import os
import re
from collections import Counter

IMPORT_MATCHING = '^(import.*)'


def main():
    folder = get_folder_from_user()
    if not folder:
        print('Impossible to search here...')
    else:
        pass

    results = search_folder(folder)
    c = Counter()
    for result in results:
        c.update(result)

    for k, v in c.items():
        print('{} {}'.format(k, v))


def parse_file(file):
    with open(file) as f:
        for line in f:
            match = re.match(IMPORT_MATCHING, line)
            if match is not None:
                yield [imports.strip() for imports in match.group()[7:].split()]
            else:
                continue


def get_folder_from_user():
    folder = input('What folder would you like to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return folder


def search_folder(folder):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item)
        elif full_item.endswith(".py"):
            yield from parse_file(full_item)
        else:
            continue


if __name__ == '__main__':
    main()
