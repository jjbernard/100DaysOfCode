import pytest
import D06


def test_ask_user_for_input(capsys):
    input_values = ['1950', '10', '5']
    wrong_input_values = ['ABDC', 'EFGH', 'IJKL']

    def correct_mock_input(s):
        print(s, end='')
        return input_values.pop(0)

    D06.input = correct_mock_input

    D06.ask_user_for_input()

    out, err = capsys.readouterr()

    assert out == "".join(['What is the earliest year of analysis for this dataset? [YYYY] ',
                           'How many directors would you like to list? ',
                           'How many movies at minimum should we consider per director? '])

    assert err == ''


def test_user_input():
    input_string = 'test'
    output_string = 'Second test'
    pass


def test_get_movies_list():
    # todo: check that it fails if no data
    # todo:
    pass
