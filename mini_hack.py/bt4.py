colors = ['Red', 'Blue', 'Green']
print("Our list of colors:", *colors, sep = ' ,')
n = int(input("If you want to view a color, please enter its number/position: "))
print(colors[n])