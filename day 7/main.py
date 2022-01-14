import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["ardvark", "baboon", "camel"]
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
    for index in range(wordLength):
        letter = randomWord[index]
        if letter == guess:
            randomWordList[index] = guess
            tracker = 1
    if tracker == 0:
        lives -= 1
        print(stages[lives])

    print(randomWordList)
    if "_" not in randomWordList:
        end_of_game = True
        print("You Win!")
    if lives == 0:
        end_of_game = True
        print("Game Over!")
