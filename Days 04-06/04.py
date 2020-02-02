from collections import Counter, namedtuple, defaultdict, deque
import random

# namedtuple

user = ('bob', 'programmer')

print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user = User(name='jj', role='fisherman')

print(user.name)
print(user.role)

print(f'{user.name} is a {user.role}')

# defaultdict

users = {'jj': 'fisherman'}

print(users['jj'])

print(users.get('jj'))

print(users.get('toto') is None)

challenges_done = [('jj', 10), ('roro', 7), ('guigui', 9),
                   ('jj', 3), ('roro', 9), ('guigui', 8)]
print(challenges_done)

challenges = defaultdict(list)

for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

# Counter

words = """Contrary to popular belief, Lorem Ipsum is not simply random text. 
It has roots in a piece of classical Latin literature from 45 BC, making it over 
2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College 
in Virginia, looked up one of the more obscure Latin words, consectetur, from a 
Lorem Ipsum passage, and going through the cites of the word in classical literature, 
discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 
"de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. 
This book is a treatise on the theory of ethics, very popular during the Renaissance. 
The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a 
line in section 1.10.32."""

words = words.split()

print(Counter(words).most_common(10))

# deque
# See jupyter notebook


