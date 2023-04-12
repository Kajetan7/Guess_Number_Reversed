#  Guess Number Reversed Game
#  Author: Kajetan Mroske
#
#  This program plays a game where the computer tries to guess a number that player has chosen
#  between 0 and 1000. The game ends when the computer correctly guesses the number or the player
#  switches the number during the game.

print('''\nThink about a number in between 0 and 1000...
I'm going to guess it in 10 moves! \n
Pick your number and start the game with enter.''')

start_ = input()  # Player initiates the game with enter.

min_ = 0  # Minimum margin for guess number is set.
max_ = 1000  # Maximum margin for guess number is set.

#  The variable option_ stores the player's feedback on each guess made by the computer.
#  There are three possible options:
#  1. "too big" if the player's number is smaller than the computer's guess.
#  2. "too small" if the player's number is larger than the computer's guess.
#  3. "you are correct" if the computer's guess is correct.
option_ = ""

#  The computer will make at most 10 guesses, which is enough given the range of marigns.
#  The game ends either when the player confirms the computer's guess or when the maximum
#  number of guesses is reached.
for i in range(11):
    if option_ == "3":
        # Player picked the option: 3 - you are correct!
        print("\n Thanks for your time! It was a good game!")
        break  # Loop breaks and program stops.
    if i == 10:
        # Player must have switched the selected number during the game.
        print("\n Don't cheat! You have switched the number! \n")
        break

    #  The computer makes a guess by selecting a number in the middle of the current margins.
    guess_ = int((max_ - min_) / 2) + min_

    #  The computer prints its guess and asks the player for feedback.
    print(f'\n I pick: {guess_}!')
    print('\n Is it the number you chose? \n')

    while True:
        #  The player enters feedback on the computer's guess.
        option_ = input('Pick one of following options: 1 - too big, 2 - too small, 3 - you are correct!')

        if option_ == "3":
            #  If the player confirms the computer's guess, the game ends.
            print("\n Yeah! I won!")
            break  # While loop breaks. Leads to program stop.
        elif option_ == "2":
            #  If the player's number is smaller than the computer's guess,
            #  the minimum margin is replaced with the guess made by the computer.
            min_ = guess_
            break
        elif option_ == "1":
            #  If the player's number is larger than the computer's guess,
            #  the maximum margin is replaced with the guess made by the computer.
            max_ = guess_
            break
        else:
            #  If the player does not select an option, the program asks again.
            continue
