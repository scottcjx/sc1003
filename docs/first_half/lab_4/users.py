""" @title user.py """
from utils import safe_stoi

# stub data
users_db = {'Test': 'Test12345', 'Jack': 'Test12345', 'Tom': 'Password1'} 


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
