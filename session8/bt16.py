print(hobby)
hobby.remove('Vainglory')
hobby.insert(0, 'Sword Art Online')
hobby.remove('Anime')
hobby.insert(4, 'Naruto')
print(*hobby, sep = ', ')

i = int(input("Enter a hobby number you want to replace: "))
n = input("Enter a new hobby: ")
hobby[i] = n
p = int(input("Which hobby number do you want to remove: "))
hobby.pop(p)
print(*hobby, sep = ', ')