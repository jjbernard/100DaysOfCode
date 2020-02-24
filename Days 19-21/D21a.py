import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


friends = 'bob joe bill steve'.split()


def friends_teams(list_of_friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(list_of_friends, r=team_size)
    else:
        return itertools.combinations(list_of_friends, r=team_size)


if __name__ == '__main__':
    # get_attendees()
    teams = friends_teams(friends, 2, True)
    for team in teams:
        print(team)
