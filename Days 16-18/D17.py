import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

name_list = [name.title() for name in NAMES]

def gen_pair(nl):
    for i in range(50):
        pairs = random.choices(nl, k=2)
        yield f'{pairs[0].split()[0]} teams up with {pairs[1].split()[0]}'


if __name__ == '__main__':
    pairs = gen_pair(name_list)
    for _ in range(10):
        print(next(pairs))
