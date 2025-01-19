import random
coin_side = ['heads', 'tails']
random_side = int(random.random() * len(coin_side))
print(f'The coin flip result was {coin_side[random_side]}')