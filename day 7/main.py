from hangman_word import word_list
import random

from hangman_art import logo
from hangman_art import stages
print(logo)


lives = 6
randomWord = random.choice(word_list)
randomWordList = []
wordLength = len(randomWord)
for letter in range(wordLength):
    randomWordList += "_"

print(randomWordList)
end_of_game = False

while not end_of_game:
    tracker = 0
    guess = input("Guess a letter: ")
    guess.lower()
    if guess in randomWordList:
        print(f"You've already guessed {guess}")
    for index in range(wordLength):
        letter = randomWord[index]
        if letter == guess:
            randomWordList[index] = guess
            tracker = 1
    if tracker == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        print(stages[lives])

    
    print(f"{' '.join(randomWordList)}")
    if "_" not in randomWordList:
        end_of_game = True
        print("You Win!")
    if lives == 0:
        end_of_game = True
        print("Game Over!")
