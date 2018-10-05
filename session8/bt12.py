hobby = ["Vainglory", "LOL", "Eroge", "Manga", "Anime"]
print(hobby)
hobby.remove('Vainglory')
hobby.insert(0, 'Sword Art Online')
hobby.remove('Anime')
hobby.insert(4, 'Naruto')
print(*hobby, sep = ', ')