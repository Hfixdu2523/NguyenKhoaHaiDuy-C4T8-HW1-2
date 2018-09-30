while True:
    n=input("Enter username: ")
    if n.isalpha():
        print("Invalid username")
    elif n.isalnum():
        if len(n) >= 8:
            if n.istitle():
                print("Valid username")
                break
            else:
                print("Invalid username")
        else:
            print("Invalid username")