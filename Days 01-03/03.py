# Create a pomodoro timer
from datetime import datetime, timedelta
from time import sleep
import os


def get_durations():
    """
        Get the duration for both the quiet time to focus and the pause between those
        quiet times
    :return: a list with 2 elements: quiet time and pause time durations
    """

    while True:
        quiet_time = input("How long would you like your focus time to last (in min)? ")

        try:
            quiet_time = int(quiet_time)
        except ValueError:
            print("You should enter a number of minutes.")
            continue

        pause_time = input("How long would you like your pause time to last (in min)? ")

        try:
            pause_time = int(pause_time)
        except ValueError:
            print("You should enter a number of minutes.")
            continue

        break

    return [quiet_time, pause_time]


def run_pomodoro():
    while True:
        answer = input("Would you like to specify Pomodoro times? [Y/N] ")

        if answer not in ['Y', 'y', 'N', 'n']:
            print("Answer must be Y (for Yes) or N (for No).")
            continue
        else:
            break

    if answer in ['Y', 'y']:
        q, p = get_durations()
    else:
        q, p = 25, 5

    starttime = datetime.today()
    qtime = timedelta(minutes=q)
    ptime = timedelta(minutes=p)

    os.system("CLEAR")
    while True:
        print("Focus time starting!\n")
        sleep(10)
        while datetime.today() < starttime + qtime:
            sleep(1)
            remain = starttime + qtime - datetime.today()
            minutes = remain.seconds // 60
            seconds = remain.seconds % 60
            os.system("CLEAR")
            print("Focus time. Time left --> {}:{}".format(str(minutes), str(seconds)))

        print("\nEnd of your quiet time. You can take a break\n")
        sleep(10)
        while datetime.today() < starttime + qtime + ptime:
            sleep(1)
            remain = starttime + qtime + ptime - datetime.today()
            minutes = remain.seconds // 60
            seconds = remain.seconds % 60
            os.system("CLEAR")
            print("Time left for break --> {}:{}".format(str(minutes), str(seconds)), end="\r", flush=False)

        starttime = datetime.today()


if __name__ == "__main__":
    run_pomodoro()
