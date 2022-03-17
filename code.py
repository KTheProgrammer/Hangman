import random

stages = ['''
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
''']

word_list = ["people", "baboon", "robot", "apple", "turtle", "boat", "riding"]
chosen_word = random.choice(word_list)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

print(stages[lives])

#Create blanks
display = []
for letter in range(len(chosen_word)):
  display.append("_")
print(f"{' '.join(display)}")

while ("_") in display:
  guess = input("Guess a letter: \n")
  guess = guess.lower()

    #Check guessed letter
  count = 0

  for letter in chosen_word:
    if guess == letter:
      display[count] = guess
    count += 1

   #If guess is not a letter in the chosen_word,
   #Then reduce 'lives' by 1. 
   #If lives goes down to 0 the game should stop and print "You lose."

  if guess not in chosen_word:
    lives -= 1
  if lives == 0:
    print(stages[lives])
    print("You Lose")
    break

  print(stages[lives])
  print(f"{' '.join(display)}")

  if not ("_") in display:
    print("You Win")
