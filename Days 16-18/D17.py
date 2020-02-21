import random
import itertools

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

name_list = [name.title() for name in NAMES]

name_reversed = [" ".join(list(reversed(name.split()))) for name in name_list]


def gen_pair():
    name_list = [name.title() for name in NAMES]
    while True:
        pairs = random.choices(name_list, k=2)
        yield f'{pairs[0].split()[0]} teams up with {pairs[1].split()[0]}'


if __name__ == '__main__':
    pairs = gen_pair()
    print(list(itertools.islice(pairs, 10)))
