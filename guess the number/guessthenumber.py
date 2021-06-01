import random
#random generation of a number between 1 and 100
lucky= random.randrange(1,100)
#reading a number from keyboard
user_guess=int(input("Guess a number between 1 and 100: "))
#using a while loop until the number is found
while user_guess != lucky :
    #checking if the entered number is either higher or lower compared to the random number
    if user_guess < lucky:
        print("You need to guess higher. Try again!")
        user_guess = int(input("\nGuess a number between 1 and 100: "))
    else:
        print("You need to guess lower. Try again!")
        user_guess = int(input("\nGuess a number between 1 and 100: "))
print("You guessed the number correctly")