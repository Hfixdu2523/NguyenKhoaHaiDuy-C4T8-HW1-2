while True:
    colors = ['Red', 'Blue', 'Green']
    print("Our list of colors:", *colors)
    n = input("What color do you want to delete? Enter its name or number: ")
    if n == str:
        z = int(n)
        if z in [0, 1, 2]:
            colors.pop(z)
            print("Updated list:", *colors)
            break
        else:
            print("Error, please re-enter")
    elif n in colors:
        
        colors.remove(n)
        print("Updated list:", *colors)
        break
        
    else:
        print("Error, please re-enter")
