import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
gamer=[rock,paper,scissor]
user=int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
print(gamer[user])
computer=random.randint(0,2)
print(f"Computer Choose:{computer}")
print(gamer[computer])
if user >= 3 or user < 0:
    print("You entered a wrong number.You lose")
elif user==computer:
    print("It is a draw.Try again.")
elif user==0 and computer==2:
    print("You win")
elif user==0 and computer==1:
    print("You lose")
elif user==1 and computer==0:
    print("You win")
elif user==1 and computer==2:
    print("You lose")
elif user==2 and computer==1:
    print("You win")
else:
    print("You lose")
