import random

win_choices = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
choices = ['rock', 'scissors', 'paper']


class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, roll):
        if self.name == roll.name:
            return 'Tie'
        elif win_choices[self.name] == roll.name:
            return 'Win'
        else:
            return 'Lose'


class Player:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.won = 0

    def win(self):
        self.won += 1


def print_header():
    print('---------------------------------------')
    print('      Rock - Paper - Scissors')
    print('---------------------------------------')
    print()


def print_name():
    name = input('What is your name? ')
    print('Nice to meet you {}'.format(name))
    print()
    return name


def game_loop(name):
    counter = 1
    while counter < 3:
        player_roll = input('What is your choice [rock], [paper] or [scissors]?  ')
        if player_roll not in choices:
            print('Sorry, try again')
            continue
        computer_roll = random.choice(choices)
        player = Player(name, Roll(player_roll))
        computer = Player("Computer", Roll(computer_roll))

        outcome = player.roll.can_defeat(computer.roll)
        print('{} chose {}'.format(player.name, player.roll.name))
        print('Computer chose {}'.format(computer.roll.name))

        if outcome == 'Tie':
            print('It\'s a tie!')
            continue
        elif outcome == 'Win':
            player.win()
            counter += 1
            print('{} won.'.format(player.name))
        else:
            computer.win()
            counter += 1
            print('{} won.'.format(computer.name))

    if player.won > computer.won:
        print("Congrats! {} won.".format(player.name))
    else:
        print("Looks like the computer beat you!")


if __name__ == '__main__':
    print_header()
    player = print_name()
    game_loop(player)
