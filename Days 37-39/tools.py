import csv
import os
from pathlib import Path
from collections import namedtuple, defaultdict
from typing import List

Record = namedtuple("Record",
                    "congress,chamber,bioguide,firstname,"
                    "middlename,lastname,suffix,birthday,"
                    "state,party,incumbent,termstart,age")


def load_data() -> List:
    current_dir = Path(os.path.dirname(__file__))
    filename = current_dir / "data/congress-terms.csv"

    data = list()
    with open(filename, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            record = parse_data(row)
            data.append(record)

    return remove_duplicate(data)


def parse_data(row: dict) -> Record:
    row['age'] = float(row['age'])
    record = Record(**row)

    return record


def remove_duplicate(data: list) -> List[Record]:
    res = defaultdict(list)
    for member in data:
        if member.bioguide not in res:
            res[member.bioguide] = member
        elif res[member.bioguide].age > member.age:
            res[member.bioguide].age = member.age
            res[member.bioguide].termstart = member.termstart
        else:
            continue

    res = [k for k in res.values()]
    return res


def find_oldest(data: list) -> List[Record]:
    return sorted(data, key=lambda x: -x.age)


def find_youngest(data: list) -> List[Record]:
    return sorted(data, key=lambda x: x.age)


def find_oldest_rep(data: list) -> List[Record]:
    data = [x for x in data if x.party == 'R']
    return sorted(data, key=lambda x: -x.age)


def find_youngest_dem(data: list) -> List[Record]:
    data = [x for x in data if x.party == 'D']
    return sorted(data, key=lambda x: x.age)
