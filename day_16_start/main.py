# OOP fundamentals, attributes and construction
import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable

hermit = Turtle()
hermit.shape('turtle')
hermit.color('black', 'purple')
turtle.forward(100)

my_screen = Screen()
# my_screen.exitonclick()

print(my_screen.canvheight)

table = PrettyTable()

table.field_names = ['Pokemon Name', 'Type']

table.add_rows([
    ['Pikachu', 'Electric'],
    ['Squirtle', 'Water'],
    ['Charmander', 'Fire']
])

table.align = 'l'

print(table)

