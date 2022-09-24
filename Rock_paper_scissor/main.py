import random

def play():
  user = input("'r' for rock, 'p' for paper. 's' for scissors ")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    print('tie')
  elif user == 'r' and computer == 'p':
    print("Computer Wins!")
  elif user == 'p' and computer == 's':
    print("Computer Wins!")
  else:
    print("You Won!")

play()