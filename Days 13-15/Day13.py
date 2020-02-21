import random

win_choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
choices = ["rock", "scissors", "paper"]


class Roll:
    def __init__(self, rtype):
        self.rtype = rtype

    def can_defeat(self, roll):
        if self.rtype == roll.rtype:
            return "Tie"
        elif win_choices[self.rtype] == roll.rtype:
            return "Win"
        else:
            return "Lose"


class Player:
    def __init__(self, name):
        self.name = name
        self.roll = None
        self.won = 0

    def set_roll(self, roll):
        self.roll = roll

    def win(self):
        self.won += 1

    def compute_outcome(self, player):
        outcome = self.roll.can_defeat(player.roll)
        print("{} chose {}".format(self.name, self.roll.rtype))
        print("{} chose {}".format(player.name, player.roll.rtype))
        return outcome


def print_header():
    print("---------------------------------------")
    print("      Rock - Paper - Scissors")
    print("---------------------------------------")
    print()


def print_name():
    name = input("What is your name? ")
    print("Nice to meet you {}".format(name))
    print()
    return name


def create_players(names):
    return Player(names[0]), Player(names[1])


def game_loop(names):
    player, computer = names
    counter = 0
    while counter < 3:
        player_choice = input("What is your choice [rock], [paper] or [scissors]?  ")
        if player_choice not in choices:
            print("Sorry, try again")
            continue

        player.set_roll(Roll(player_choice))
        computer.set_roll(Roll(random.choice(choices)))
        outcome = player.compute_outcome(computer)

        if outcome == "Tie":
            print("It's a tie!")
            continue
        elif outcome == "Win":
            player.win()
            counter += 1
            print("{} won.".format(player.name))
        else:
            computer.win()
            counter += 1
            print("{} won.".format(computer.name))

    print('{} score: {}'.format(player.name, player.won))
    print('{} score: {}'.format(computer.name, computer.won))

    if player.won > computer.won:
        print("Congrats! {} won.".format(player.name))
    else:
        print("Looks like the computer beat you!")


if __name__ == "__main__":
    print_header()
    player = print_name()
    players = create_players([player, "Computer"])
    game_loop(players)
