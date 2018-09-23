mth = int(input("Enter month of the year: "))
if 1 < mth < 5:
    print("spring")
elif 4 < mth < 8:
    print("summer")
elif 7 < mth < 10:
    print("autumn")
elif mth > 12:
    print("Period does not exist")
elif mth < 1:
    print("Period does not exist")
else: 
    print("winter")