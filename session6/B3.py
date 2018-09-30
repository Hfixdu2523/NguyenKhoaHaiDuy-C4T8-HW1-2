while True:
    print("This is a question to test you")
    print("0 legs")
    print("4 legs")
    print("8 legs")
    print("12 legs")
    n = input("How many legs does a spider have? Enter answer : ")
    print(n)
    if n == "0 legs":
        print("You are wrong")
        break
    elif n == "4 legs":
        print("You are wrong")
        break
    elif n == "8 legs":
        print("You are correct")
        break
    elif n == "12 legs":
        print("You are wrong")
        break
    else:
        print("Invalid answer. Please re-enter")