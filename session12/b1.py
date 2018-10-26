# a) print("*"*20)

# b) n = int(input("Enter the number of stars you want: "))
# print("*" * n)

# c) print(9 * "x * ")

# d) n = int(input("Enter the number of stars and 'x' you want: "))
# print(n * "x * ")

# e) print()     ->  empty line

# f) for i in range(3):
#        print("*" * 7)

# g)    # n = int(input("Enter the number of stars in a row: "))
        # m = int(input("Enter number of rows: "))
        # for i in range(m):
        #     print("*" * n)

# h)            # for y in range(5):
                #     for x in range(5):
                #         if x == 2 and y == 2:
                #             print("x", end=" ")
                #         else:
                #             print("-", end=" ")
                            
                #     print()

n = int(input("Enter width of table: "))
m = int(input("Enter height of table: "))
for x in range(n):
    for y in range(m):
        g = int(input("Enter x co-ordinate of X: "))
        l = int(input("Enter y co-ordinate of X: "))
        if x == g and y == l:
            print("X", end = " ")
        # else:
        #     print("-", end = " ")
print()


                    
    

