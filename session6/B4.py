while True:
    string = input("Enter username: ")
    if string.isalpha():
        print("Invalid username")
    elif string.isalnum():
        print("Valid username")
        break
    else:
        print("Invalid username")