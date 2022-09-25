import random
import time

level_number = 100
level = 1
new_level_number = 100
computer_number = random.randint(1, level_number)

while True:
    time.sleep(0.5)
    player_input = input(f"Guess a number between 1 and {new_level_number}: ")
    player_number = int(player_input)
    if player_number == 69:
        time.sleep(0.5)
        print("Come on be an adult for a moment...")
    if player_number == computer_number:
        time.sleep(0.5)
        print(f"You GUESSED IT !!! Number is {computer_number}")
        new_level = level + 1
        time.sleep(1)
        print(f"Next level - {new_level}")
        computer_number = random.randint(1, new_level_number + 100)
        new_level_number += new_level_number

    elif player_number > computer_number:
        time.sleep(0.5)
        print("your guess is too high. Try again")
    else:
        time.sleep(0.5)
        print("your guess is too low. Try again")
