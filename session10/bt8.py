game = {
    "name": "Vainglory",
    "description": "MOBA",
    "status": "frequent updates",
    "features": "3v3, 5v5"
}
print(game)
n = input("Enter key name from dictionary: ")
if n in game:
    print(game[n])
else:
    print("Error 404")