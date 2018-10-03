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
                    print("Invalid password")
            else:
                print("Invalid password")
        else:
            print("Invalid email")
    else:
        print("Invalid email")   
