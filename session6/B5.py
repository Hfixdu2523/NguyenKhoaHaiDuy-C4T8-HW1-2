while True:
    string = input("Enter username: ")
    if string.isalpha():
        print("Invalid username")
    elif string.isnumeric():
        if len(string) >= 8:
            print("Valid username")
            break
        else:
            print("Invalid username")
    elif string.isalnum():
        if len(string) >= 8:
            print("Valid username")
            break
        else:
            print("Invalid username")
    else:
        print("Invalid username")