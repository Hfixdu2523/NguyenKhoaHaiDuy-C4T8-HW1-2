game_slangs = {
    "GLHF": '''A term which is used as a friendly method to tell
team mates to try their best and win the game. However it is 
also used to indicate that the player is trolling''',
    "FEEDING": '''A series of actions in-game that show intentional
bad behaviour and making enemy team so powerful from the gold 
gathered that your team has no way to win''',
    "GG": '''Good game: expressing that you have enjoyed a good game
or just to annoy the losing team after you win the game'''
}
for x in game_slangs:
    print(x)

while True:
    print("If you want to exit, type 'EXIT'")
    n = input("Enter a game slang you want to look up: ").upper()
    if n in game_slangs:
        print(game_slangs[n])
    if n == "EXIT":
        print("You have exited succesfully")
        break
    else:
        print("Not found")