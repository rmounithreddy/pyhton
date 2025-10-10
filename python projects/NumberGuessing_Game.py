import random
def number_guessing_game():
    print("welcome to the number guessing game")
    print("i am thinking of a number between 1 to 100")
    number = random.randint(1,100)
    attempts = 10
    while attempts > 0:
        guess = int(input("make a guess:"))
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")
        else:
            print(f"congratualations you guessed the number {number} correctly")
            break
        attempts -=1
        print(f"you have {attempts} attempts left")
    if attempts == 0:
        print(f"sorry, you have used all your attempts. the number was {number}")
number_guessing_game()
