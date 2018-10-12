game = {
    "name": "Vainglory",
    "description": "MOBA",
    "status": "frequent updates",
    "features": "3v3, 5v5"
}
print(game)

n = input("Enter key you want to delete: ")
if n in game:
    del game[n]
    print(game)
else:
    print("Error 404")