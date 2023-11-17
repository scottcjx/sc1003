import random

def conv_str_to_int_safe(inp: str):
    """ converts string to integer, catching invalid strings
    """
    try:
        outp = int(inp)
    except:
        print("Wrong input format. Please try again.")
        return False, None
    
    return True, outp

def guessing_game():
    """ main function for guessing game
    """
    n = random.randint(1, 9)
    
    print("dbg:: ", n)

    for i in range(3):
        valid, guess = conv_str_to_int_safe(input("Enter an integer from 1 to 9: "))
        if (not valid):
            continue
        elif (guess == n):
            print(f"Congratulations. You guessed it by {i+1} trials!")
            print("You can start the game now")
            return True
        elif (guess < n):
            print("guess is low")
        else:
            print("guess is high")

    print("Sorry, you exceed the trial limit. Failed.")
    return False

def calculate_sum():
    """ main function for calculate sum game
    """
    n = random.randint(55, 66)

    correct_ans = 0
    for i in range(5):
        correct_ans = correct_ans + (n + i)
        print("dbg:: ", correct_ans, "->", n+i)

    print("dbg:: ", n , n+4, " -> ", correct_ans)

    print(f"Please calculate the sum of 5 integers start from {n}")
    valid, guess = conv_str_to_int_safe(input("Please enter your answer: "))
    if (not valid):
        pass
    elif (guess != correct_ans):
        print("Sorry, wrong answer. Failed.")
    elif (guess == correct_ans):
        print("You can start the game now")
    else:
        print("unknown error")


if __name__ == "__main__":
    """ main game loop
    """
    print("Please select one of the following quizzes:")
    print("\t1. Number guessing")
    print("\t2. Calculate sum")

    valid, game_choice = conv_str_to_int_safe(input("\n"))
    if (not valid):
        print("Wrong input format. Please try again.")
    elif (game_choice == 1):
        guessing_game()
    elif (game_choice == 2):
        calculate_sum()
    else:
        print("Wrong option. Bye.")
