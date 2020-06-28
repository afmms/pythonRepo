# Write your code here
import random

print("H A N G M A N")
while(True):
    play_exit = input('Type "play" to play the game, "exit" to quit: ')

    if(play_exit == "play"):
        word_list = 'python', 'java', 'kotlin', 'javascript'
        word = random.choice(word_list)
        word_as_list = list(word)
        masked_word = ('-' * (len(word)))
        masked_word_as_list = list(masked_word)
        attempts_left = 8
        user_won = False
        guessed_leters = set()

        while((attempts_left > 0) and (not user_won)):  
            print("\n" + masked_word)
            guess = input("Input a letter: ")    
            if(len(guess) != 1):
                print("You should input a single letter")
            elif(guess in guessed_leters):
                print("You already typed this letter")
            elif(guess.isupper() or not guess.isalpha()):
                print("It is not an ASCII lowercase letter")
            elif(guess not in word):
                attempts_left-=1
                guessed_leters.add(guess)
                print(f"No such letter in the word. You have {attempts_left} attempts left.")
            else:
                guessed_leters.add(guess)
                while(guess in word):
                    pos = word.index(guess)
                    word_as_list[pos] = "-"
                    word = "".join(word_as_list)
                    masked_word_as_list[pos] = guess
                    masked_word = "".join(masked_word_as_list)
                    
                if("-" not in masked_word):
                    user_won = True

    else:
        print("It's not a game then!")
        break

    if(user_won):
        print("You guessed the word {}!".format(masked_word))
        print("You survived!")
    else:
        print("You are hanged!")
    break;