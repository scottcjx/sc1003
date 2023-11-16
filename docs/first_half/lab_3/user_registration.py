import json
import os

users_db = {'Test': 'Test12345', 'Jack': 'Test12345', 'Tom': 'Password1'} 
SPECIAL_CHAR_SET = '[@_!#$%^&*()<>?/\|}{~:]'

def conv_str_to_int_safe(inp: str):
    """ converts string to integer, catching invalid strings
    """
    try:
        outp = int(inp)
    except:
        print("Wrong input format. Please try again.")
        return False, None

    return True, outp


""" ui choose login
"""
print("Please select one of the following quizzes:")
print("\t1. User Registration")
print("\t2. User Login")

valid, choice = conv_str_to_int_safe(input(""))
if (not valid):
    pass
elif (choice == 1):
    """ ui for registration of users
    """

    print("User registration:")

    valid_usern = 0
    while not valid_usern:
        usern = input("insert your username: ")
        if usern in users_db.keys():
            print("The user exists. Please choose another user name.")
        else:
            break
        
    passwd = ""
    passwd_ok = 0

    while not passwd_ok:
        print("Input your password")
        print("1.the password has at least one upper case letter")
        print("2.the password has at least one lower case letter")
        print("3.the password has at least one digit")
        print("4.its length is more than 8 ")
        print("5.the password has at least one special character")

        passwd = input("")

        condi_length = 0
        condi_ucase = 0
        condi_lcase = 0
        condi_digit = 0
        condi_special_char = 0

        condi_length_tmp = 0
        for letter in passwd:
            if letter.isdigit():
                condi_digit = 1
            elif letter.islower():
                condi_lcase = 1
            elif letter.isupper():
                condi_ucase = 1
            elif letter in SPECIAL_CHAR_SET:
                condi_special_char = 1
            else:
                pass
                # print("unknown err: ", letter)
            condi_length_tmp += 1

        condi_length = (condi_length_tmp > 7)

        passwd_ok = bool(condi_length and condi_ucase and condi_lcase and condi_digit and condi_special_char)

        if not passwd_ok:
            print("Your password is weak. Please enter a new password")
        else:
            print("Your password is strong enough. User registered.")
            users_db[usern] = passwd
            break
    
    print("The users in system", users_db)
elif (choice == 2):
    """ login ui
    """
    if users_db == {}:
        print("err: no users in database, please register first!")
        exit()

    usern = input("Input user name: ")
    if not usern in users_db.keys():
        print("User not existing.")
        exit()
    
    passwd = input("Input Password: ")
    passwd_valid = (users_db[usern] == passwd)

    while not passwd_valid:
        passwd = input("Wrong password, input again: ")
        passwd_valid = (users_db[usern] == passwd)
    
    print("Welcome back, Test, You can start the game. ")
else:
    print("Wrong option. Bye.")

