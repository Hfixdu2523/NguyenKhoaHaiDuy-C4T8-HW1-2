hobby = ["Vainglory", "LOL", "Eroge", "Manga", "Anime"]
print(hobby)
new_hobby = input('Include another hobby: ')
hobby.append(new_hobby)
print(hobby)
print(*hobby, sep = ' | ')
print(hobby[0])
print(hobby[-1])
print(hobby[-2])