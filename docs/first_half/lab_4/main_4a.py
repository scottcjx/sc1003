import random

# global var
users_db = {'Test': 'Test12345', 'Jack': 'Test12345', 'Tom': 'Password1'} 

# util functions ================================================
def safe_stoi(inp: str):
    """ @docstring
    @title
    converts string to integer, catching invalid strings

    @returns (is inp a valid int): bool, (int(inp)): int
    """
    try:
        # try to convert str to int
        outp = int(inp)
    except:
        # catches all exception

        # print("Wrong input format. Please try again.")
        return False, None
    
    return True, outp

# users functions ================================================

def hasSpecialChar(inp: str) -> bool:
    """ @docstring
    @title hasSpecialChar
    checks if special char in string
    @returns (? special char in string): boolean
    """
    SPECIAL_CHAR_SET = '[@_!#$%^&*()<>?/\|}{~:]'

    for special_char in SPECIAL_CHAR_SET:
        # for each special char
        # check if char is in input.
        if special_char in inp:
            """ @note
            return true and exit function;
            this is because we only want to know if there
            exists special char in input; having more than
            1 will not change its output; safe computing
            power and return upon finding char in input
            """
            return True
    
    # this code block will only execute if no special char found in inp, 
    # therefore return false
    return False


def isStrongPassword(inp: str) -> bool:
    """ @docstring
    @title isStrongPassword
    checks if string meets conditions for strong password
    @return (if string meets conditions for strong password)
    """
    condi_length = 0
    condi_ucase = 0
    condi_lcase = 0
    condi_digit = 0

    # checks condition seperately
    condi_special_char = 1 if hasSpecialChar(inp) else 0

    condi_length_tmp = 0
    for letter in inp:
        if letter.isdigit():
            condi_digit = 1
        elif letter.islower():
            condi_lcase = 1
        elif letter.isupper():
            condi_ucase = 1
        else:
            pass
        condi_length_tmp += 1

    condi_length = (condi_length_tmp > 7)

    # for a strong password, ALL condition must be met
    ret = bool(condi_length and condi_ucase and condi_lcase and condi_digit and condi_special_char)
    return ret


def userLogin():
    """ @docstring
    @title userLogin
    @return (user logged in)
    """

    # catch if users_db not instantiated
    if users_db == {}:
        print("err: no users in database, please register first!")
        return False
    
    # gets user input for username
    usern = input("Input user name: ")

    # if username not in dictionary, user doesnt exist
    if not usern in users_db.keys():
        print("User not existing.")
        return False
    
    passwd = input("Input Password: ")
    passwd_valid = (users_db[usern] == passwd)

    while not passwd_valid:
        passwd = input("Wrong password, input again: ")
        passwd_valid = (users_db[usern] == passwd)
    
    print("Welcome back, Test, You can start the game. ")
    return True


def userRegistration(username: str, password: str) -> bool:
    """ @docstring
    @title userRegistration
    @return
    """

    """
    advanced function to check that username indeed does not exist in
    system. if it does, it means input is invalid and throws Assertion Exception
    (no need to return False as program will exit, showing this error)
    """
    assert not (username in users_db.keys())

    # set new element in dictionary;
    # key: username, value: password
    users_db[username] = password

    return True


def getNewUserName() -> str:
    """ @docstring
    @title getNewUserName
    @return
    """
    
    # define loop condition as username being valid; define as false
    valid_usern = 0
    while not valid_usern:
        """
        while we have NOT gotten a valid username, we keep requesting
        for a valid username
        """
        usern = input("insert your username: ")

        # check if usernmae already in dictionary
        valid_usern = usern not in users_db.keys()

        if not valid_usern:
            print("The user exists. Please choose another user name.")
        else:
            return usern
            # if username NOT in dict, assume as a new and valid username


def getStrongPassword() -> str:
    """ @docstrig
    @title getStrongPassword
    @return (strong password): str
    """

    # define passwd input
    passwd = ""

    # define loop condition as password being strong; define as false
    passwd_ok = 0
    while not passwd_ok:
        """
        while we have NOT gotten a strong password, we keep requesting
        for a strong password
        """

        print("Input your password")
        print("1.the password has at least one upper case letter")
        print("2.the password has at least one lower case letter")
        print("3.the password has at least one digit")
        print("4.its length is more than 8 ")
        print("5.the password has at least one special character")

        passwd = input("")
        passwd_ok = isStrongPassword(passwd)

        if not passwd_ok:
            print("Your password is weak. Please enter a new password")
        else:
            print("Your password is strong enough. User registered.")
            return passwd
            break

# games functions ================================================

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

# main functions ================================================

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
