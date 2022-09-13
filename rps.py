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

scissiors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
your_choice=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissiors.\n"))
computer_choice= random.randint(0,2)
list=[rock, paper, scissiors]
print("Your_choice_is")
if your_choice > 2:
  print("Invalid Number, You Lose!!!!!")
else:
  print(list[your_choice])
  print("computer Choice is")
  print(list[computer_choice])
  
  if your_choice ==0 and computer_choice ==2:
    print("You win")
  elif your_choice ==0 and computer_choice==1:
    print("you lose")
  elif your_choice ==2 and computer_choice==0:
    print("you lose")
  elif your_choice ==2 and computer_choice==1:
    print("you win")
  elif your_choice ==1 and computer_choice==0:
    print("you win")
  elif your_choice ==computer_choice:
    print("Tie, please try again")
  else:
    print("you lose")
