# Create a pomodoro timer
from datetime import datetime, timedelta
from time import sleep
import os
import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()

    run_pomodoro(stdscr)

    stdscr.refresh()
    stdscr.getkey()


def curses_input(stdscr, x, y, string_input, size):
    curses.echo()
    stdscr.addstr(x, y, string_input)
    stdscr.refresh()
    input = stdscr.getstr(x + 1, y, size)
    return input


def get_durations(stdscr):
    """
        Get the duration for both the quiet time to focus and the pause between those
        quiet times
    :return: a list with 2 elements:
            - quiet_time
            - pause_time
    """

    while True:
        stdscr.clear()
        quiet_time = curses_input(stdscr, 0, 0, "How long would you like your focus time to last (in min)? ", 2)

        try:
            quiet_time = int(quiet_time)
        except ValueError:
            stdscr.addstr(1, 0, "You should enter a number of minutes.")
            stdscr.refresh()
            continue

        stdscr.clear()
        pause_time = curses_input(stdscr, 0, 0, "How long would you like your pause time to last (in min)? ", 1)

        try:
            pause_time = int(pause_time)
        except ValueError:
            stdscr.addstr(1, 0, "You should enter a number of minutes.")
            stdscr.refresh()
            continue

        break

    return [quiet_time, pause_time]


def run_pomodoro(stdscr):
    while True:
        stdscr.clear()
        answer = curses_input(stdscr, 0, 0, "Would you like to specify Pomodoro times? [Y/N] ", 1)

        if answer not in ['Y', 'y', 'N', 'n']:
            stdscr.addstr(1, 0, "Answer must be Y (for Yes) or N (for No).")
            continue
        else:
            break

    if answer in ['Y', 'y']:
        q, p = get_durations(stdscr)
    else:
        q, p = 25, 5

    starttime = datetime.today()
    qtime = timedelta(minutes=q)
    ptime = timedelta(minutes=p)

    # os.system("CLEAR")
    while True:
        stdscr.clear()
        stdscr.addstr(0,0, "Focus time!")
        while datetime.today() < starttime + qtime:
            sleep(1)
            remain = starttime + qtime - datetime.today()
            minutes = remain.seconds // 60
            seconds = remain.seconds % 60
            # os.system("CLEAR")
            stdscr.addstr(1, 0, "Focus time. Time left --> {}:{}".format(str(minutes), str(seconds)))

        stdscr.addstr(2, 0, "End of your quiet time. You can take a break")
        while datetime.today() < starttime + qtime + ptime:
            sleep(1)
            remain = starttime + qtime + ptime - datetime.today()
            minutes = remain.seconds // 60
            seconds = remain.seconds % 60
            # os.system("CLEAR")
            stdscr.addstr(3, 0, "Time left for break --> {}:{}".format(str(minutes), str(seconds)))

        starttime = datetime.today()


if __name__ == "__main__":
    stdscr = curses.initscr()
    wrapper(main(stdscr))
