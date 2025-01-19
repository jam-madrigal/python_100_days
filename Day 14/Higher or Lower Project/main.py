# make a list of dictionaries of vtubers along with their sub count and something about them in another file
import random
from vtubers import data
from art import logo
from art import vs
# import that file

# import the art,
# make a function to select a random vtuber and then pop it off the list
def choose_random_vtuber(youtubers):
    """Selects a random vtuber from a list, then pops it off that list so it can't be chosen again"""
    return youtubers.pop(random.randint(0, len(youtubers) - 1))


choose_random_vtuber(data)
# make a variable to hold the players score, starts at 0
score = 0
# store A and B outside the loop, if A is not empty, then A = the current B, and B = random, else A is random, B random
a_vtuber = {}
b_vtuber = {}
guessed_correct = True
print(logo)
while guessed_correct:
# make the A the previous B, make the dictionary entry after the current A the next B
    if a_vtuber != {}:
        a_vtuber = a_vtuber
        b_vtuber = choose_random_vtuber(data)
    else:
        a_vtuber = choose_random_vtuber(data)
        b_vtuber = choose_random_vtuber(data)
# show the logo at the top, the VS in between A and B while comparing
# ask the user to compare a random vtuber to another random vtuber, when a vtuber is stored in a new variable in the loop...
    print(f'Compare A: {a_vtuber["name"]}, {a_vtuber["bio"]} Their agency is {a_vtuber["agency"]}.')
    print(vs)
    print(f'Vtuber B: {b_vtuber["name"]}, {b_vtuber["bio"]} Their agency is {b_vtuber["agency"]}.')
    guess = input('Who has more subscribers? Type "A" or "B"').lower()
    guessed_correct = False
# if they get it wrong, tell them they were wrong and their final score and end the game
# keep going if they guess correctly, increase their score by one,
