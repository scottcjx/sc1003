import json
import os

users_db = {}

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

def special_char_chk(inp: str):
    """ checks if special char in string
    """
    for special_char in SPECIAL_CHAR_SET:
        if special_char in inp:
            return True
    return False

def str_checker(inp: str):
    """ checks if string meets conditions for strong password
    coding ex. 3a
    """
    condi_length = 0
    condi_ucase = 0
    condi_lcase = 0
    condi_digit = 0
    condi_special_char = 1 if special_char_chk(inp) else 0

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
            # print("unknown err: ", letter)
        condi_length_tmp += 1

    condi_length = (condi_length_tmp > 7)

    # special char check
    ret = bool(condi_length and condi_ucase and condi_lcase and condi_digit and condi_special_char)
    # ret = bool(condi_length and condi_ucase and condi_lcase and condi_digit)
    # print(inp, "-> ", ret)
    return ret

def ui_register_user_2b():
    """ ui for registration of users
    """
    print("User registration:")
    usern = input("insert your username: ")
    
    passwd = ""
    passwd_ok = 0

    while not passwd_ok:
        print("Input your password")
        print("1.the password has at least one upper case letter")
        print("2.the password has at least one lower case letter")
        print("3.the password has at least one digit")
        print("4.its length is more than 8 ")

        passwd = input("")
        passwd_ok = str_checker(passwd)

        if not passwd_ok:
            print("Your password is weak. Please enter a new password")
        else:
            print("Your password is strong enough. User registered.")

def init_db(fp: str):
    if not os.path.exists(fp):
        with open(fp, 'w') as f:
            json.dump({}, f)
    with open(fp, 'r') as f:
        data = json.load(f)
        return data

def deinit_db(fp: str):
    with open(fp, 'w') as f:
        json.dump(users_db, f)

def ui_register_user():
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
        passwd_ok = str_checker(passwd)

        if not passwd_ok:
            print("Your password is weak. Please enter a new password")
        else:
            print("Your password is strong enough. User registered.")
            users_db[usern] = passwd
            break
    
    print("The users in system", users_db)

def ui_login():
    """ login ui
    """
    if users_db == {}:
        print("err: no users in database, please register first!")
        return False

    usern = input("Input user name: ")
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

def ui_choose_login_register():
    """ ui choose login
    """
    print("Please select one of the following quizzes:")
    print("\t1. User Registration")
    print("\t2. User Login")

    valid, choice = conv_str_to_int_safe(input(""))
    if (not valid):
        pass
    elif (choice == 1):
        ui_register_user()
    elif (choice == 2):
        ui_login()
    else:
        print("Wrong option. Bye.")

if __name__ == "__main__":
    users_db = init_db("./lab_3/users_db.json")
    # print("dbg:: The users in system", users_db)
    ui_choose_login_register()
    deinit_db("./lab_3/users_db.json")
