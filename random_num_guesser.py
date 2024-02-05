import random

player_attempts = 0
correct_answer = False

random_number = random.randrange(0,10)

player_input = int(input("I have randomly chosen a number between 0 and 10, what do you think it is? "))

while correct_answer == False:
    if player_input == random_number:
        correct_answer = True
        print(f"Thats right! The random number was indeed {random_number}. It only took you {player_attempts} attempts! Congrats!")
    else:
        player_input = int(input("Sorry, that was the wrong number, please try again. "))
        player_attempts += 1