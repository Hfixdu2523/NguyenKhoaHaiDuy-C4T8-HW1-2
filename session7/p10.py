n = int(input("Enter a month:"))
if n in (1, 3, 5, 7, 8, 10, 12):
    print("There are 31 days in the month")
elif n in (4, 6, 9, 11):
    print("There are 30 days in the month")
elif n == 2:
    print("There are 28 days in the month")
else:
    print("Đoán xem :)")