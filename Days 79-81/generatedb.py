from contextlib import contextmanager
import sqlite3

name = ""


@contextmanager
def create_db(name: str) -> sqlite3.Cursor:
    try:
        conn = sqlite3.connect(f'{name}.db')
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close()


def prompt_for_name() -> str:
    name = input("What would you like to name your test db file? ")
    return name


if __name__ == '__main__':
    name = prompt_for_name()
    with create_db(name) as cursor:
        cursor.execute("""CREATE TABLE test_table (col1 TEXT, col2 TEXT, col3 TEXT, col4 INT)""")

        print(f"{name}.db as been created")
