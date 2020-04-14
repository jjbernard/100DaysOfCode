import sqlite3


def main():
    connection = sqlite3.connect('addressbook.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE Details (name TEXT, address TEXT, phone_number INT) """)

    connection.close()


if __name__ == '__main__':
    main()
