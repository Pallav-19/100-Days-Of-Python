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

#Write your code below this line 👇
computerChoice = random.randint(0,2)
choices = [rock,paper,scissors]
yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
print(choices[yourChoice])
print(f"Computer Chose: \n{choices[computerChoice]}")
resultss = str(computerChoice)+str(yourChoice)
if resultss == "00" or resultss == "11" or resultss == "22" :
  print("Its a Draw!")
elif resultss == "01" or resultss == "12" or resultss == "20":
  print("You Win!")
else:
  print("You Lose!")


