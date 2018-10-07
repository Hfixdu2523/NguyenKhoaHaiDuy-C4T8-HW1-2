print("Account Setup:")

n = input("Enter username: ")
while True:
    m = input("Enter email: ")
    if "@" in m:
        if ".com" in m:
            p = input("Enter password :")
            if len(p) >= 8:
                if p.isalnum():
                    o = input("Confirm password :")
                    if p == o:
                        print("Valid password, Welcome user!")
                        break
                    else:
                        print("Invalid password") 
                else:
                    print("Password must contain alphabet letters and numbers")
            else:
                print("Password muust be at least 8 letters long")
        else:
            print("Invalid email")
    else:
        print("Invalid email")   
