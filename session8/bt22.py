while True:
    hobby = ["Vainglory", "LOL", "Eroge", "Manga", "Anime", 'Netflix', 'Dota', 'Something']
    print(hobby)
    n = input("Among 4 methods C,R,U,D, choose one you want to do: ").upper()
    if n == "C":
        new_hobby = input("What do you want to add as a hobby? ")
        hobby.append(new_hobby)
        print(hobby)
        break
    elif n == "R":
        for i, item in enumerate(hobby):
            print(i + 1, ".", item)
            
            if len(hobby) == 0:
                print("List is empty")
                break
        break
    elif n == "U":
        upd = int(input("Enter a hobby number you want to replace: "))
        new = input("Enter a new hobby: ")
        hobby[upd] = new
        print(*hobby, sep = " ," )
        break
    elif n == "D":
        delete = input("Enter a hobby you want to remove:")
        if delete in hobby:
            hobby.remove(delete)
            print(hobby)
            break
        else:
            print("Error. Please re-enter")
    else:
        print("Error, please try again")