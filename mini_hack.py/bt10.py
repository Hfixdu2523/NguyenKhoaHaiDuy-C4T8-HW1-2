num = [12, 35, 69, 70, 81, 92, 47]
print(*num, sep = ' ,')
for item in num:
    if item % 2 == 0:
        print("Even numbers:", item)
    else:
        print("Odd number:", item)