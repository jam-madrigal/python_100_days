import random
# make a random number between 0 and 100, store it in a computer's number variable
computer_number = random.randint(0, 100)
# ask the user to select a difficulty, adjust lives to 10 for easy, 5 for hard
difficulty = input('Select a difficulty. Type "easy" or "hard".\n').lower()
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print("Invalid difficulty selection. Ending the game.")
    lives = 0
# while the game is running, prompt the user to guess a number
game_running = True
while game_running:
    if lives == 0:
        print('Game over.')
        game_running = False
    user_guess = int(input('Guess a number from 0 and 100:\n'))
    if user_guess == computer_number:
        print('You won!')
        game_running = False
# if they guess wrong, decrease lives by one, else tell them they won and end the game
    if user_guess != computer_number:
        if user_guess > computer_number:
            lives -= 1
            print(f'Too high. Guess again\n You have {lives} guesses remaining')
        elif user_guess < computer_number:
            lives -= 1
            print(f'Too low. Guess again. You have {lives} guesses remaining.')

# inform the user if the guess was too high or too low, and tell them how many lives remain
# if they guess correctly, tell them they won and end the game
# if their lives ever hit 0, end the game and tell them they lost