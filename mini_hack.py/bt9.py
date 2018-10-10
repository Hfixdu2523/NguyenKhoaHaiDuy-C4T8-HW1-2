m = input("Enter a list of numbers, separated by a ' ':")
n = m.split()


print("List of entered numbers:", *n)

print("Sum of numbers entered:", sum(int(i) for i in n))
