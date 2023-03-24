#  Guess Number Reversed Game
#  Author: Kajetan Mroske

import random


print('''\nThink about a number in between 0 and 1000...
I'm going to guess it in 10 moves! \n
Pick your number and start the game with enter.''')
start_ = input()

min_ = 0
max_ = 1000

guess = int((max_ - min_) / 2) + min_

print(f'I pick: {guess}!')
print('Is it the number you chose?')
print('Pick one of following options: 1 - too big, 2 - too small, 3 - you are correct!')
