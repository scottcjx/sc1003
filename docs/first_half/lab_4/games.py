""" @title games.py """
from utils import safe_stoi
import random


def guessingNumber() -> bool:
    """ @docstring
    @title guessingNumber
    @return (did user pass the game)
    """

    # define n as a random number from 1 - 9 (inclusive)
    n = random.randint(1, 9)

    # loop 3 times, setting i as current iteration of loop (starts from 0)
    for i in range(3):

        # my own function to safely convert str to int.
        # returns if str is valid int, int(answer)
        valid, guess = safe_stoi(input("Enter an integer from 1 to 9: "))

        if (not valid):
            # user entry not valid int
            
            # warn user and continue to next loop iteration
            print("Wrong input format. Please try again.")
            continue

        elif (guess == n):
            # guess == n, user guessed n correctly

            # note that {i+1} this is because i starts from 0
            print(f"Congratulations. You guessed it by {i+1} trials!")
            print("You can start the game now")
        
            # exit function
            return True
        
        elif (guess < n):
            # guess lesser than n
            print("guess is low")

        else:
            # if not same, and not lesser, only logical logic is that
            # guess > n
            print("guess is high")

    # this code block will only be executed if user has not guessed correctly,
    # therefore we can assume that user failed
    print("Sorry, you exceed the trial limit. Failed.")
    return False


def calculateSum() -> bool:
    """ @docstring
    @title calculateSum
    @return (did user pass the game)
    """

    # define n as a random number from 55 to 66 (inclusive)
    n = random.randint(55, 66)

    # define calculated answer as 0
    correct_ans = 0

    # loop for 5 times, setting i as loop counter (starting from 0)
    for i in range(5):
        """
        add (n + i) to correct answer; where
        n is the random number given,
        i is the current loop iter.

        eg: n = 55
        correct_ans = (55 + 0) + (55 + 1) + (55 + 2) + (55 + 3) + (55 + 4)
        """
        correct_ans = correct_ans + (n + i)

    print(f"Please calculate the sum of 5 integers start from {n}")

    # safely conv str to int
    valid, guess = safe_stoi(input("Please enter your answer: "))

    # catch if user input is invalid
    if (not valid):
        print("Wrong input format. Please try again.")
    elif (guess != correct_ans):
        print("Sorry, wrong answer. Failed.")
        return False
    elif (guess == correct_ans):
        print("You can start the game now")
        return True
    else:
        # code should theoretically not reach here; but would be good to know if
        # some error to pop up here
        print("unknown error")

    return False

