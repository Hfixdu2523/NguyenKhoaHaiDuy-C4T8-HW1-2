while True:
    string = input("Enter username: ")
    if string.isalpha():
        print("Valid username")
        break
    else:
        print("Invalid username")
        