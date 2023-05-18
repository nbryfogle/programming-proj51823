from random_word import RandomWords

r = RandomWords()

def game():
    word: str = r.get_random_word()
    word_list = list(word)
    guessed_list = ("_ "*len(word)).split()
    letters_guessed = []
    lives = 15

    while True: 
        print("".join(guessed_list))
        letter = input("Guess a letter: ")
        if letter in letters_guessed:
            print("You already guessed that letter!")
            print(f"Guessed letters: {', '.join(letters_guessed)}")
            continue

        letters_guessed.append(letter)

        if letter in word:
            for i in word_list:
                if letter == i:
                    index = word_list.index(letter)
                    word_list[index] = "_"
                    guessed_list[index] = letter
            if "_" not in guessed_list:
                print(f"You guessed the word with {lives} lives left!")
                break

        else:
            lives -= 1
            if lives == 0:
                print(f"Game over! The word was \"{word}\"")
                break
            else:
                print(f"Letter is not in the word. You have {lives} lives left.")

        
        
game()