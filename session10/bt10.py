game = {
    "name": "Vainglory",
    "description": "MOBA",
    "status": "frequent updates",
    "features": "3v3, 5v5"
}
print(game)

n = input("Enter key you want to update: ")
if n in game:
    m = input("Enter the value to be updated: ")
    game[n] = m 
    print(game)
else:
    print("Error 404")