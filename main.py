import random



def number_guessing_game():

    #welcome message
    print("////////////////////////////////////")
    print("welcome to the number guessing game")
    print("//////////////////////////////////////")

    highest_number = 100
    lowest_number = 1

    random_number = random.randint(lowest_number, highest_number)

    print(f"i am thinking of a number between {lowest_number} and {highest_number}")

    while True:
        guess = int(input("You can enter your guess here: "))


        if guess > highest_number: print("oops that number is too high, pick a number between 1-100")
        elif guess < lowest_number: print("oops that number is too low, pick a number between 1-100")
        elif guess > random_number: print("too high")
        elif guess < random_number: print("too low")
        else: print("congrats you got the number")



number_guessing_game()





