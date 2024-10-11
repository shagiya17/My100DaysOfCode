import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
print(game_images[user])

opp_choice = random.randint(0,2)
print(f"Computer chose: {game_images[opp_choice]}")

if user >= 3 or user < 0:
    print("You typed a invalid number you lose!")
elif user == 0 and opp_choice == 2:
    print("You win!")
elif opp_choice == 0 and user == 2:
    print("You lose!")
elif opp_choice > user:
    print("You lose!")
elif user > opp_choice:
    print("You win!")
elif opp_choice == user:
    print("It's a draw!")
