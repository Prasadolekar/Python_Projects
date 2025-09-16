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
choices=[rock,paper,scissors]
a=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if a<0 and a>2:
    print("Invalid Selection")
    exit()
print(choices[a])
rand=random.randint(0,2)
print("Computer Chooses")
print(choices[rand])
if a==rand:
    print("Tie")
elif (a==0 and rand==2) or (a==1 and rand==0) or (a==2 and rand==1):
    print("You win!")
else:
    print("You lose!")