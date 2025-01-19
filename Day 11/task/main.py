import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []
game = 'running'

def deal_card():
    return random.choice(cards)

def calculate_score(cards_held):
    if sum(cards_held) == 21:
        print(f'Game over')
        game = 'over'
        return 0
    elif sum(cards_held) > 21:
        for card in cards_held:
            if card == 11:
                card = 1
                return sum(cards_held)
    else:
        return sum(cards_held)

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

while game != 'over':
    print(f'The user total is: {calculate_score(user_cards)}')
    print(f'The computer total is: {calculate_score(computer_cards)}')




