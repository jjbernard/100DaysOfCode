def print_header():
    print('---------------------------------------')
    print('      Rock - Paper - Scissors')
    print('---------------------------------------')
    print()


def print_name():
    name = input('What is your name? ')
    print('Nice to meet you {}'.format(name))
    print()


if __name__ == '__main__':
    print_header()
    print_name()
