# make a list of dictionaries of vtubers along with their sub count and something about them in another file
from vtubers import data
from art import logo
from art import vs
# import that file
print(data)
print(logo)
print(vs)
# import the art,
# make a variable to hold the players score, starts at 0
# show the logo at the top, the VS in between A and B while comparing
# ask the user to compare a random vtuber to another random vtuber, when a vtuber is stored in a new variable in the loop...
# store A and B outside the loop, if A is not empty, then A = the current B, and B = random, else A is random, B random
# pop it off the possible options in the list, so it doesn't repeat and compare itself to itself
# if they get it wrong, tell them they were wrong and their final score and end the game
# keep going if they guess correctly, increase their score by one,
# make the A the previous B, make the dictionary entry after the current A the next B
