from utils import safe_stoi
from users import userLogin, userRegistration, getNewUserName, getStrongPassword
from games import guessingNumber, calculateSum


def getUserChoice():
    prompt = \
        "Please select one of the following options: \n" + \
        "\t 1. User registration \n" + \
        "\t 2. User Login \n" + \
        "\t 3. Play the game as a guest\n"
    
    # get choice from user
    choice = input(prompt)

    # converts str to int safely
    valid, choice = safe_stoi(choice)

    # set choice as -1 if choice not sucessfully conv to int
    choice = choice if valid else -1

    return choice


def guestQuiz():
    quizChoice = chooseQuiz()
    isPass = takeQuiz(quizChoice)
    if isPass:
        print("Congratulations. You can start the game.")  


def chooseQuiz():
    prompt = \
        "Dear Guest, you have to pass one quiz to play the game. \n" + \
        "Please select one of the following quizzes: \n" + \
        "\t 1. Number guessing \n" + \
        "\t 2. Calculate sum \n"

    # get choice from user
    choice = input(prompt)

    # converts str to int safely
    valid, choice = safe_stoi(choice)

    # set choice as -1 if choice not sucessfully conv to int
    choice = choice if valid else -1

    return choice


def takeQuiz(choice):
    if choice == 1:
        isPass = guessingNumber()
        
    elif choice == 2:
            isPass = calculateSum() 
    return isPass  


def main():
    choice = getUserChoice()
    if choice == 1:
        print("User registration:")
        userRegistration(getNewUserName(),getStrongPassword())

    elif choice == 2:
        userLogin()
        
    elif choice == 3:
        guestQuiz()
    else:
        print("Wrong input format. Please try again.")


# call main
main()
