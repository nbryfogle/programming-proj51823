import random

num = random.randint(1, 8213947213094781327041327)

tries = 0

min_num = 1
max_num = 8213947213094781327041327

while True:
    guess = random.randint(min_num, max_num)
    print(guess)
    tries += 1
    if tries % 100 == 0:
        print("min", min_num)
        print("max", max_num)

    if guess == num:
        print(f"It took the bot {tries} attempts to guess the number!")
        exit()
    
    if guess < num:
        min_num = guess + 1
    
    if guess > num:
        max_num = guess - 1
    