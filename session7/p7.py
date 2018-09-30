from turtle import*
speed(5)
n = int(input("Enter a number: "))
m = 360/n
for i in range(n):
    forward(60)
    right(m)

mainloop()