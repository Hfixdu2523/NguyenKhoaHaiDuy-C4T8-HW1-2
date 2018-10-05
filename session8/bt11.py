hobby = ["Vainglory", "LOL", "Eroge", "Manga", "Anime"]
print(hobby)
hobby.remove('Vainglory')
hobby.insert(0, 'Sword Art Online')
print(*hobby, sep = ', ')