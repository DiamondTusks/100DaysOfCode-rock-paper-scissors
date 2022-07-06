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

#Write your code below this line 👇
import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computer = random.randint(0,2)

if player >= 0 and player <= 2:

  if player == 0 and computer == 0:
    print(rock)
    print("Computer chose:")
    print(rock)
    print("Draw!")
  elif player == 0 and computer == 2:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win!")
  elif player == 0 and computer == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print ("You lose!")
    
  elif player == 1 and computer == 1:
    print(paper)
    print("Computer chose:")
    print(paper)
    print ("Draw!")
  elif player == 1 and computer == 0:
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win!")
  elif player == 1 and computer == 2:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print ("You lose!")
    
  elif player == 2 and computer == 2:
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("Draw!")
  elif player == 2 and computer == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win!")
  elif player == 2 and computer == 0:
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose!")
  
else:
  print("Your choice is not valid. You lose!")


