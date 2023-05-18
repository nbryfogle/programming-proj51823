import random

print("Welcome to the Random Number Game")

secret_number = random.randint(1, 100000)

guesses = 1000000

while guesses != 0:
    print(f"You have {guesses} guesses remaining.")
    
    guess = int(input("Guess the Number: "))
    guesses -= 1

    if secret_number == guess: 
        print("You're Winner :)")
        exit()
    
    else:
        print(":(")
        
        if guess > secret_number:
            print('Guess Too High')
        elif guess < secret_number:
            print('Guess Too Low')

print("You're Lose")
print(f"The number was {secret_number}")