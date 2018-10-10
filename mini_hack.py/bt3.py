colors = ['Red', 'Blue', 'Green']
print("Our colors:", *colors, sep = ' ,')
n = input("What color do you want to add? ")
colors.append(n)
print("Our new colors list:", *colors, sep = ' ,')
