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

print('Welcome to rock, paper, scissors.')
choice = int(input("Select 0 for rock, 1 for paper, 2 for scissors\n"))
# get a random choice for the computer
choices = [rock, paper, scissors]
cpu_choice = random.randint(0, 2)
print(cpu_choice)
# make win conditions and lose conditions, else draw
if choice not in (0, 1, 2):
    print("Invalid choice")
elif choice == cpu_choice:
    print(f'The cpu chose {choices[cpu_choice]}\n Draw')
elif choice == 0:
    if cpu_choice == 2:
        print(f'The cpu chose {choices[cpu_choice]}\n You win!')
    else:
        print(f'The cpu chose {choices[cpu_choice]}\n You lose')
elif choice == 1:
    if cpu_choice == 0:
        print(f'The cpu chose {choices[cpu_choice]}\n You win!')
    else:
        print(f'The cpu chose {choices[cpu_choice]}\n You lose')
else:
    if cpu_choice == 1:
        print(f'The cpu chose {choices[cpu_choice]}\n You win!')
    else:
        print(f'The cpu chose {choices[cpu_choice]}\n You lose')
