from data import us_state_abbrev, states

NOT_FOUND = 'N/A'


def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    states = enumerate(states)
    nth_item_list = []
    for i, item in states:
        if (i + 1) % n == 0:
            nth_item_list.append(item)

    return nth_item_list


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return us_state_abbrev[state_name]
    except KeyError:
        return NOT_FOUND


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    if isinstance(data, list):
        return max(data, key=len)
    else:
        return max([k for k, _ in data.items()], key=len)


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list. The resulting list
       has both sorted, so:
       ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
       (see also test_combine_state_names_and_abbreviations)"""

    sorted_abbrev = {k: v for k, v in sorted(us_state_abbrev.items(),
                                             key=lambda item: item[1])}
    states.sort()
    return [v for i, (k, v) in enumerate(sorted_abbrev.items()) if i < 10] + states[-10:]


if __name__ == '__main__':
    print(get_every_nth_state(states=states, n=10))
    print(get_state_abbrev('California'))
    print(get_state_abbrev('bogus'))
    print(get_longest_state(states))
    print(get_longest_state(us_state_abbrev))
    print(combine_state_names_and_abbreviations())
