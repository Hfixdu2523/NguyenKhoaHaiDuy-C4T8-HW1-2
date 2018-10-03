while True:
    import random
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = a + b + random.randint(-1, 1)
    print(a, "+", b, "=", c)
    n = (input("True or False? "))
    if c == a + b:
        if n == "True":
            print("That's correct")
            break
        elif n == "False":
            print("That's incorrect")
    if c != a + b:
        if n == "True":
            print("That's incorrect")
        elif n == "False":
            print("That's correct")
            break