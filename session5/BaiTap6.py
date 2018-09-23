log = input("Enter Username: ")
print(log)
if log != "techkids":
    print("You are not superuser")
elif log == "techkids":
    pss = input("Enter password: ")
    print(pss)
    if pss != "codethechange":
        print("Invalid password")
    elif pss == "codethechange":
        print("Welcome, superuser!")

