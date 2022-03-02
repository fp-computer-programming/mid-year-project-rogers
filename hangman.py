# Author: SMR (AMDG) 03/2/22
# First importing the random module. Might need to use later on.
import random
# Creating a variable named hangman which will be the display of the hangman game.
hangman = ['''
HANGMAN - Vegetables 

   -----
   |   |
       |
       |
       |
       |
=========''', '''
HANGMAN - Vegetables 

  -----
  |   |
  O   |
      |
      |
      |
=========''', '''
HANGMAN - Vegetables 

  -----
  |   |
  O   |
  |   |
      |
      |
=========''', '''
HANGMAN - Vegetables 

  -----
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
HANGMAN - Vegetables 

  -----
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
HANGMAN - Vegetables  

  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
HANGMAN - Vegetables 

  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Defining the first function which will be the vegetable list.
def random_vegi():
# Words from the vegetable list to choose from    
    vegi_list = ['cabbage', 'eggplant', 'carrot', 'artichoke', 'beet', 'broccoli', 'cauliflower', 'cucumber',
             'lettuce', 'mushroom', 'onion', 'pea', 'pepper', 'potato', 
             'pumpkin', 'radish', 'zucchini','corn','sweetpotato','celery','squash','spinach',]

# From this list choose a random vegetable    
    word = random.choice(vegi_list)

    return word

# Defining a function to take 4 different arguments. These arguments need to include the hang, the missed letters, the correct letters, and also the secret word chosen from the function above.
def display(hangman, letters_missing, letters_correct, word_chosen):

# Prints the length of the missed letters   
    print(hangman[len(letters_missing)])
    print()

# Will print out the missed letters
    print('Missed Letters:', end=' ')

# Creating a for loop that for each letter in missed letters, print out the letter with ' '     
    for letter in letters_missing:
        print(letter, end=' ')
 
 # Finally print a new line   
    print("\n")

# Need to create blanks in order to display which letter is missing from each spot 
    blanks = '_' * len(word_chosen)

# This function will replace the blank with the correctly guessed letters from the user
    for index in range(len(word_chosen)):  
# Creating an if statement         
        if word_chosen[index] in letters_correct:
# Finally creating the variable blanks to show replacement            
            blanks = blanks[:index] + word_chosen[index] + blanks[index+1:]
# for loop in order to show the secret word with spaces in between each letter
    for letter in blanks:  
        print(letter, end=' ')
    print("\n")

# Defining a function to prompt for the user's input
def getGuess(alreadyGuessed):
# While the function is true    
    while True:
    # Guess a letter    
        guess = input('Guess a letter: ')
    # Automatically convert the input into lowercase    
        guess = guess.lower()
    # In case the user enters something that is longer than one character, tell the user to re-enter one letter    
        if len(guess) != 1:
            print('Please enter a single letter.')
    # If the guess was already guessed, prompt the user to input another letter    
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
    # If the guess is not a letter, prompt the user to input a letter        
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
    # If none of this occurs then finally return the guess    
        else:
            return guess

# Creating a function asking the user if he/she wants to play again
def playAgain():
# Input statement on a new line asking if the user would like to play again.     
    return input("\n Would you like to play again? ").lower().startswith('y')

# creating blank space
letters_missing = ''
# creating blank space
letters_correct = ''
# the secret word variable is equal to the random choice selected in the function above
word_chosen = random_vegi()
# game is not over yet
game_completed = False
# while true
while True:
# display the board again   
    display(hangman, letters_missing, letters_correct, word_chosen)
# The guess is equal to the getguess of missed letters plus the correct letters
    guess = getGuess(letters_missing + letters_correct)
# if statement of guess in secret word
    if guess in word_chosen:
    # Correct letters is equal to itself plus guess  
        letters_correct += guess
    # if all of the letters are found is true
        foundAllLetters = True
        for i in range(len(word_chosen)):
            if word_chosen[i] not in letters_correct:
                foundAllLetters = False
                break
        if foundAllLetters:
        #Prints out that the user found the secret word on a new line    
            print('\nYes! The secret word is "' + word_chosen + '"! Congratulations!')
      
            game_completed = True
    # If you didn't win, you lost. 
    else:
        letters_missing = letters_missing + guess
    # If user guessed too many times 
        if len(letters_missing) == len(hangman) - 1:
        # Display the board    
            display(hangman, letters_missing,letters_correct, word_chosen)
           # Will print out that the user has ran out of final guesses.
            print('You have run out of guesses! \nYou had ' + str(len(letters_missing)) + ' guesses and ' + str(len(letters_correct)) + ' correct guesses. The word was "' + word_chosen + '" good luck next time.')
            game_completed = True
# If the game is done
    if game_completed:
        if playAgain():
            letters_missing = ''
            letters_correct = ''
            game_completed = False
            word_chosen = random_vegi()
        else:
            break