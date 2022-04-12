import datetime
import time


def header():
    print('------------------------')
    print('    POMODORO TIMER')
    print('------------------------')

def user_choice():
    choice = input("Choose your timeout: "
                   "[1] Pomodoro 25 min; "
                   "[2] Short break 5 min; "
                   "[3] Long break 10 min; "
                   "[4] Exit: ")
    if choice == '1':
        pomodoro()
    elif choice == '2':
        short_break()
    elif choice == '3':
        long_break()
    elif choice == '4':
        print('good luck!')
        quit()
    else:
        print('Please, try again!')


def pomodoro():
    timer = datetime.timedelta(minutes=25)
    while timer:
        print(f'Pomodoro timer {str(timer)}')
        time.sleep(1)
        timer -= datetime.timedelta(seconds=1)
    print('Time is up!')

def short_break():
    timer = datetime.timedelta(minutes=5)
    while timer:
        print(f'Short break timer {str(timer)}')
        time.sleep(1)
        timer -= datetime.timedelta(seconds=1)
    print('Time is up!')

def long_break():
    timer = datetime.timedelta(minutes=10)
    while timer:
        print(f'Long break timer {str(timer)}')
        time.sleep(1)
        timer -= datetime.timedelta(seconds=1)
    print('Time is up!')



if __name__ == '__main__':
    header()
    user_choice()
