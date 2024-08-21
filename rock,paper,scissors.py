import random
import sys

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
game_icon = [rock, paper, scissors]

inp = int(input('Enter your choice 0 for Rock, 1 for Paper, 2 for Scissors: '))
if inp <=2:
      print("Your choice")
      print(game_icon[inp])
else :
       print (" Your choice is not valid")
       sys.exit()

rand =  random.randint(0, 2)
out = rand
print("Computer choice")
print(game_icon[rand])

if inp == out:

    print(inp)
    print(out)
    print('Its a tie!')
elif inp == 0 and out == 1:

    print(inp)
    print(out)
    print('You lose!')
elif inp == 0 and out == 2:

    print(inp)
    print(out)
    print('You win!')
elif inp == 1 and out == 0:

    print(inp)
    print(out)
    print('You win!')
elif inp == 1 and out == 2:

    print(inp)
    print(out)
    print('You lose!')
elif inp == 2 and out == 0:

    print(inp)
    print(out)
    print('You loose!')
elif inp == 2 and out == 1:

    print(inp)
    print(out)
    print('You win!')
