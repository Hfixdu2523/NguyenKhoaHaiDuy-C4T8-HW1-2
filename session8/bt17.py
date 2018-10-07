hobby = ["Vainglory", "LOL", "Eroge", "Manga", "Anime"]
print(hobby)
hobby.remove('Vainglory')
hobby.insert(0, 'Sword Art Online')
hobby.remove('Anime')
hobby.insert(4, 'Naruto')
print(*hobby, sep = ', ')

i = int(input("Enter a hobby number you want to replace: "))
n = input("Enter a new hobby: ")
hobby[i] = n
while True:
    p = str(input("Correctly enter the hobby that you want to remove: "))
    if p in hobby:
        hobby.remove(p)
        print(*hobby, sep = ', ')
        break
    else:
        print("Hobby already removed. Please enter another hobby")