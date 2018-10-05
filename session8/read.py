items = ['com', 'pho', 'chao', 'com rang']
print(items)
print(*items, sep = ', ')

print("Index 1")
print(items[1])

print("Index 0")
print(items[0])

print("Index -2")
i = int(input("Enter Index: "))
print(items[i])