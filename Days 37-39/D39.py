"""
In this file, we will analyse data coming from the FiveThirtyEight github
repo located at https://github.com/fivethirtyeight.
More specifically, we will look at the "congress-age" dataset which records
all US congress members from Jan 1947 to Feb 2014.
The readme from 538 is here:
https://github.com/fivethirtyeight/data/tree/master/congress-age
"""

import tools

# todo: (optional) go further with Pandas?
# todo: (optional) explore async with Dask dataframe

def main():
    print("Analysis of the US Congress members from 1947 to 2014")
    print()
    data = tools.load_data()

    print("The 5 oldest members of Congress at the beginning of "
          "their mandate")
    for i, member in enumerate(tools.find_oldest(data)[:5]):
        print(f'{i + 1}. {member.firstname} {member.lastname} who started in '
              f'{member.termstart} at {member.age}')

    print()
    print("The 5 youngest members of Congress at the beginning of "
          "their mandate")
    for i, member in enumerate(tools.find_youngest(data)[:5]):
        print(f'{i + 1}. {member.firstname} {member.lastname} who started in '
              f'{member.termstart} at {member.age}')

    print()
    print("The 5 oldest members of Congress at the beginning of "
          "their mandate who are Rep.")
    for i, member in enumerate(tools.find_oldest_rep(data)[:5]):
        print(f'{i + 1}. {member.firstname} {member.lastname} who started in '
              f'{member.termstart} at {member.age}')

    print()
    print("The 5 youngest members of Congress at the beginning of "
          "their mandate who are Dem.")
    for i, member in enumerate(tools.find_youngest_dem(data)[:5]):
        print(f'{i + 1}. {member.firstname} {member.lastname} who started in '
              f'{member.termstart} at {member.age}')


if __name__ == '__main__':
    main()
