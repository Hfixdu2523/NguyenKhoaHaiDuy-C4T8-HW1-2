import random
pool = ("batman", "superman", "kirito", "asuna", "goku", "iron man", "captain america")
word = random.choice(pool)
list_word = list(word)
print("Answer is among these words: ", pool)
quizz = []
for i in range(len(list_word)):
    ran_char = random.choice(list_word)
    quizz.append(ran_char)
    list_word.remove(ran_char)
print(*quizz)
while True:
    guess = input("Enter your guess: ")
    if guess == word:
        print("Congrats, you are right!")
        break
    else:
        print("Oof, you might wanna try again")


# while word:
#     position = random.randrange(len(word))
#     jumble += word[position]
#     word = word[:position] + word[(position + 1):]
    
# print(jumble)

    