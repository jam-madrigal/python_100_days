# TODO-1: Ask the user for input
program_running = True
bidders = {}
while program_running:
    name = input('Enter your name:\n')
    bid = int(input('Enter your bid:\n'))
# TODO-2: Save data into dictionary {name: price}
    bidders[name] = bid
# TODO-3: Whether if new bids need to be added
    cont = input(f"Are there more bidders? Enter 'yes' or 'no'.\n").lower()
    if cont == 'no':
        program_running = False
# TODO-4: Compare bids in dictionary
        winner = max(bidders)
        print(f'The winning bidder is {winner}')



