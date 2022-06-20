
Login_or_register = input("enter login or register")

if Login_or_register.lower() == "login":
    filename = "D:\\guvi\\password\\text.txt"

    with open(filename) as new_list:
        User_database = new_list.read()

    name = input("Enter a username")
    passwd = input("enter the password")
    c = (name, passwd)
    if str(c) in User_database:
        print("Logged in")
    else:
        print("username and password does not match ")


elif Login_or_register.lower() == "register":
    def __registration__(username=input("enter username"), password=input("Enter password")):
        # username
        values = {}
        condition = "@."
        condition_1 = "@"
        condition_2 = "."
        l = list(username)
        validation_username = True
        while validation_username is True:
            if username.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "!", "#", "$", "%", "^", "&")):
                print("user name shoud start wit a alphabet")
                validation_username = False
            elif condition in username:
                print("@ and . should not be adjacent")
            elif not any(ch in condition_1 for ch in username):
                print("username should have @ symbol ")
                validation_username = False
            elif not any(ch in condition_2 for ch in username):
                print("username should have . symbol ")
                validation_username = False
            elif (l.index(".") < l.index("@")):
                print(". should not be before @ for a user name ")
                validation_username = False
            else:
                print("Username is valid")
                break
            # password

        specialsymbols = ["@", "#", "$", "%", "&", "*"]
        valiation = True
        while valiation is True:
            if len(password) < 5:
                print("Password should have at least five characters")
                valiation = False

            elif len(password) > 16:
                print("Password length should be not more than sixteen  characters")
                valiation = False

            elif not any(char.isdigit() for char in password):
                print("password should contain at least one number")
                valiation = False

            elif not any(char.isupper() for char in password):
                print("password should contain at least one upper case letter")
                valiation = False

            elif not any(char.islower() for char in password):
                print("password should contain at least one lower case letter")
                valiation = False

            elif not any(char in specialsymbols for char in password):
                print("password should contain at least one special symbol")
                valiation = False
            else:
                print("password and username is valid and Registered ")
                break
        # data storage
        values = username, password
        filr1 = open("D:\\guvi\\password\\text.txt", "a+")
        data = str(values)
        filr1.write(data)
    __registration__()














