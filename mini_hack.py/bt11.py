m = input("Enter a list of numbers, separated by a ' ':")
n = m.split()
print("List of entered numbers:", *n, sep = ' ,')
for item in n:
    g = int(item)
    if g % 2 == 0:
        print("Even numbers:", item)
    else:
        print("Odd number:", item)