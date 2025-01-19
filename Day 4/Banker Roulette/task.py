import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = int(random.random() * len(friends))

print(friends[random_index])

# you can also just use the built-in random.choice() method
# print(random.choice(friends))