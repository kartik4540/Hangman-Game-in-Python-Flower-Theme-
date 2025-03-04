#Hangman project
##Kartik-Mittal

import random
import time

Initial Steps to invite in the game:
print("\nWelcome to Hangman Game\n")
print("\nTheme FLowers Name\n")
name = input("Enter your good name: ")
print("Hello dear " + name + "! Best of Luck For the Game!")

print("Ready !!!\nThe game is about to start!\n Let's play Hangman!")

The parameters we require to execute the game:
def main():
global count
global display
global word
global already_guessed
global length
global play_game
words_to_guess = ["Pansies","Primrose","Marigold","Snapdragon Flowers","Geranium Flowers","Sunflower","Begonia","Petunia","Chrysanthemum","Sweet pea","Winter Viola flowers","Zinnia","Winter Jasmine","English Primrose","Vinca","Impatiens","Cornflower","Celosia","Red Poppies","Rose","Day Lily","Peony Flowers","Shasta Daisy","Lavender","Lilac Bush","Hibiscus","Hydrangea","Azalea","Rhododendron","Lily","Crocus Flowers","Tulips","Daffodils","Dahlia","Kalanchoe","Cacti","Christmas Cactus","Snowdrops","Bluebells","Iris"]
word = random.choice(words_to_guess)
length = len(word)
count = 0
display = '_' * length
already_guessed = []
play_game = ""

A loop to re-execute the game when the first round ends:
def play_loop():
global play_game
play_game = input("Do You want to play again? y = yes, n = no \n")
while play_game not in ["y", "n","Y","N"]:
play_game = input("Do You want to play again? y = yes, n = no \n")
if play_game == "y":
main()
elif play_game == "n":
print("Thanks For Playing! We expect you back again!")
exit()

Initializing all the conditions required for the game:
def hangman():
global count
global display
global word
global already_guessed
global play_game
limit = 5
guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
guess = guess.strip()
if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
print("Invalid Input, Try a letter\n")
hangman()

swift
Copy code
elif guess in word:
    already_guessed.extend([guess])
    index = word.find(guess)
    word = word[:index] + "_" + word[index + 1:]
    display = display[:index] + guess + display[index + 1:]
    print(display + "\n")

elif guess in already_guessed:
    print("Try another letter.\n")

else:
    count += 1

    if count == 1:

        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 2:
       
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 3:
       
       print("   _____ \n"
             "  |     | \n"
             "  |     |\n"
             "  |     | \n"
             "  |      \n"
             "  |      \n"
             "  |      \n"
             "__|__\n")
       print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    elif count == 4:
       
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

    elif count == 5:
        
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("Wrong guess. You are hanged!!!\n")
        print("The word was:",already_guessed,word)
        play_loop()

if word == '_' * length:
    print("Congrats! You have guessed the word correctly!")
    play_loop()

elif count != limit:
    hangman()
main()

hangman()
