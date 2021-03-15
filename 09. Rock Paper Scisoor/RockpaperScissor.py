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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock,paper,scissor]
user = int(input("What do u choose? Type 0 for rock, 1 for paper and 2 for scissor \n"))
if user >=3 or user < 0:
    print("Invalid choice")
else:
    print(img[user])
    computer = random.randint(0,2)
    print("Computer choose:\n")
    print(img[computer])
    if user == 0 and computer == 2:
        print("You Win")
    elif computer == 0 and user == 2:
        print("You Loose")
    elif user > computer:
        print("You win")
    elif computer > user:
        print("You Loose")
    elif computer == user:
        print("Its a draw")
