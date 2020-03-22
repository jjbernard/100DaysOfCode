"""
In this file, we will analyse data coming from the FiveThirtyEight github
repo located at https://github.com/fivethirtyeight.
More specifically, we will look at the "congress-age" dataset which records
all US congress members from Jan 1947 to Feb 2014.
The readme from 538 is here:
https://github.com/fivethirtyeight/data/tree/master/congress-age
"""

import tools

# todo: create a method to load data
# todo: create a method to adjust data types from the CSV file
# todo: create questions
# todo: answer questions
# todo: (optional) go further with Pandas?
# todo: (optional) explore async with Dask dataframe

def main():
    print("Analysis of the US Congress members from 1947 to 2014")
    print()
    data = tools.load_data()

    print(tools.find_oldest(data)[:5])

    print("The 5 oldest members of Congress at the beginning of their mandate")
    print("The 5 youngest members of Congress at the beginning of their mandate")
    print("The 5 oldest members of Congress at the beginning of their mandate who are Rep.")
    print("The 5 youngest members of Congress at the beginning of their mandate who are Dem.")



if __name__ == '__main__':
    main()
