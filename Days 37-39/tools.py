import csv
import os
from pathlib import Path
from collections import namedtuple
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

    return data


def parse_data(row: dict) -> Record:
    row['age'] = float(row['age'])

    record = Record(**row)

    return record


def find_oldest(data: list) -> List:
    sorted(data, key=lambda x: -x.age)
    return data


def find_youngest(data: list) -> List:
    sorted(data, key=lambda x: x.age)
    return data
