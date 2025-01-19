import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw = []
shuffled_pw = ''

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for char in range(nr_letters):
    pw += letters[random.randint(0, len(letters) - 1)]
for char in range(nr_symbols):
    pw += symbols[random.randint(0, len(symbols) - 1)]
for char in range(nr_numbers):
    pw += numbers[random.randint(0, len(numbers) - 1)]
for char in range(0, len(pw)):
    random_index = random.randint(0, len(pw) - 1)
    shuffled_pw += (pw.pop(random_index))

print(shuffled_pw)