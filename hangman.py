# Write your code here
import random

list_of_words = ['python', 'java', 'kotlin', 'javascript']
random.seed()
word = random.choice(list_of_words)
print("H A N G M A N")
stat = ""
while 1:
    stat = input('Type "play" to play the game, "exit" to quit: ')
    if stat == "exit":
        break
    elif stat == "play":
        guessed = set()
        arr = ["-" for x in range(len(word))]
        guessed_str = "-" * len(word)
        MAX_TRY = 8
        while MAX_TRY != 0 and guessed_str != word:
            print()
            print(guessed_str)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif guess in guessed:
                print("You already typed this letter")
            elif not guess.islower():
                # print("Please enter a lowercase English letter")
                print("It is not an ASCII lowercase letter")
            elif guess in word:
                for x in range(len(word)):
                    if guess == word[x]:
                        arr[x] = word[x]
                s = ""
                for x in arr:
                    s += x
                guessed_str = s
            else:
                # print("That letter doesn't appear in the word")
                print("No such letter in the word")
                MAX_TRY -= 1
            guessed.add(guess)
        if guessed_str == word:
            print()
            print(guessed_str)
            print("You guessed the word!")
            print("You survived!")
            print()
        else:
            print("No such letter in the word")
            print("You lost!")
            print()
