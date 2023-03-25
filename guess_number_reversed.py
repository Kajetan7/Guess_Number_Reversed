#  Guess Number Reversed Game
#  Author: Kajetan Mroske

import random


print('''\nThink about a number in between 0 and 1000...
I'm going to guess it in 10 moves! \n
Pick your number and start the game with enter.''')
start_ = input()

min_ = 0
max_ = 1000
option_ = ""

for i in range(11):
    if option_ == "3":
        print("\n Thanks for your time! It was a good game!")
        break
    if i == 10:
        print("\n Don't cheat! You have switched the number! \n")
        break
    guess_ = int((max_ - min_) / 2) + min_
    print(f'\n I pick: {guess_}!')
    print('\n Is it the number you chose? \n')
    while True:
        option_ = input('Pick one of following options: 1 - too big, 2 - too small, 3 - you are correct!')
        if option_ == "3":
            print("\n Yeah! I won!")
            break
        elif option_ == "2":
            min_ = guess_
            break
        elif option_ == "1":
            max_ = guess_
            break
        else:
            continue
