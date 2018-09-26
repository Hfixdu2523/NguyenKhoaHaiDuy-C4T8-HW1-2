import math
print("ax^2 + bx + c = 0")
a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
print(a, b, c)
if a == 0:
    print("Equation can't be solved due to conditions")
if a != 0:
    delta = (b**2 - 4*a*c)
    print(delta)
    if delta < 0:
        print("There is no solution")
    elif delta == 0:
        x1 = x2 = -b/2*a
        print("Solutions for x are: ", x1, x2)
    else:
        x1 = (-b - ((delta)**1/2)/2*a)
        x2 = (-b + ((delta)**1/2)/2*a)
        print("Solutions for x are: ", x1, x2)