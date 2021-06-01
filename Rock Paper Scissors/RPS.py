import random
users_pick = input("Enter a choice (rock, paper, scissors): ")
possible_choices = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_choices)
print(f"\nYou chose {users_pick}, computer chose {computer_action}.\n")