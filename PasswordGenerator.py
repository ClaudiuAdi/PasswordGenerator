import random
import string


def u_letters(upp_letters):
    """

    :param upp_letters:
    :return: a list of random uppercase letters
    """
    return list("".join([random.choice(string.ascii_uppercase) for _ in range(upp_letters)]))


def l_letters(low_letters):
    """

    :param low_letters:
    :return: a list of random lowercase letters
    """
    return list("".join([random.choice(string.ascii_lowercase) for _ in range(low_letters)]))


def numeric(nr):
    """

    :param nr:
    :return: a list of random numbers
    """
    return list("".join([random.choice(string.digits) for _ in range(nr)]))


def symbols(sign):
    """

    :param sign:
    :return: a list of random symbols
    """
    return list("".join([random.choice(string.punctuation) for _ in range(sign)]))


def password_gen():
    """
    function that creates the password
    :return: return the numbers of:
        digits,lowercase and uppercase letters,symbols and the status of the overflow of characters
    """
    overflow = False
    long = int(input("How long do you want your password to be?: "))

    nrs = int(input("How many numbers do you want your password to have?: "))
    n = numeric(nrs)
    print("--------------------")
    print("You have {} characters left".format(long - nrs))
    print("--------------------")
    low_letters = int(input("How many letters do you want you password to have?: "))
    low = l_letters(low_letters)
    print("--------------------")
    print("You have {} characters left".format(long - nrs - low_letters))
    print("--------------------")
    upp_letters = int(input("How many uppercase letters do you want?: "))
    upp = u_letters(upp_letters)
    print("--------------------")
    print("You have {} characters left".format(long - nrs - low_letters - upp_letters))
    print("--------------------")
    symb = int(input("How many symbols do you want?(ex: #$@&+): "))
    s = symbols(symb)

    if nrs + low_letters + upp_letters + symb > long:
        overflow = True
        print("To many characters!")

    return n, low, upp, s, overflow


def chat():
    """
    The chat related stuff
    :return:
    """

    response = input("Do you want to save your password?(Y/N)").upper()
    while response not in ["Y", "N"]:
        response = input("I don't seem to understand...would you like to enter your response again?: ").upper()
    if response == "N":
        print("That is sad..")
    else:
        print("That is good!!")

    choice = input("Do you want another password?(Y/N): ").upper()
    while choice not in ["Y", "N"]:
        choice = input("I don't seem to understand...would you like to enter your response again?: ").upper()

    if choice == "N":
        print("Ok then. Have a nice day!")
        return False, response, choice
    else:
        return True, response, choice


def password_maker():
    """
    This is the main function
    :return:it returns the password
    """

    # the list with the passwords
    codes = []
    # the option to end the program if the user doesnt want to get another password
    ok = True
    while ok:

        # the strings with their contents and the overflow variable
        numbers, low_letters, upp_letters, signs, over = password_gen()

        # condition to go again if the password its not as long as he wanted at the start(in case the user chose wrong)
        if over is True:
            continue

        # making the password
        password = numbers + low_letters + upp_letters + signs
        random.shuffle(password)

        # printing the initial password
        print("                  " + "-" * (len(password) + 6))
        print("Your password is: |  {}  |".format("".join(password)))
        print("                  " + "-" * (len(password) + 6))

        ok, response, choice = chat()

        # saving the password if the user is happy with his new password
        if response == "Y":
            codes.append("".join(password))

        # if the user doesnt want another password, it displays the passwords that he saved (if he saved)
        if choice == "N":
            if len(codes) != 0:
                print("YOUR PASSWORD(S): ")
                for i in codes:
                    print(' ' + '-' * (len(i) + 5))
                    print("|  {}  |".format(i))
                    print(' '+'-' * (len(i) + 5))
            else:
                print("Unfortunately, no passwords were good enough for you!")


if __name__ == '__main__':
    password_maker()
