while True:
    num = [3, 45, 61, 25, 18, 71]
    n = int(input("Enter a number: "))
    if n in num:
        print(num.index(n))
        break
    else:
        print("Number not in list")
