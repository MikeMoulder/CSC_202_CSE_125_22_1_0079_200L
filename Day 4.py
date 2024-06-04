#Rock Paper Scissors

import  random
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


output = [rock, paper, scissors]

print("Welcome To Rock Paper Scissors By Moulder")
userInput = input("0 For Rock, 1 For Paper, 2 For Scissors: ")

if(int(userInput) < 3 and int(userInput) >= 0):
    value = int(userInput)
    print(f"User Played " + output[value])

    computerInput = random.randint(0, 3);
    print("Computer Played " + output[computerInput])

    #DecideWinner
    if(value == 0 and computerInput == 2):
        print("You Win!")
    elif (computerInput > value):
        print("You got thrased by a bot!")
else:
    print("Invalid Input")