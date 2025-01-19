import art
def add(n1, n2):
    return n1 + n2

# TODO: Create functions for subtract, multiply, and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add the functions as values for their operator characters
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = ''
calculating = True
print(art.logo)

while calculating:
    if num1 == '':
        num1 = int(input('Enter the first number:\n'))
    else:
        print(f'The first number is: {num1}')
    operation = (input(f'Enter the type of calculation you would like to use:\n "+"\n, "-"\n, "*"\n, "/"\n '))
    num2 = int(input('Enter the second number:\n'))
    result = operations[operation](num1, num2)
    print(f'The result of {num1} {operation} {num2} is: {result}')

    answer = input('Would you like to continue with the previous result as the first number? Type "yes" or "no". '
                   'Type "quit" to stop calculating.\n')
    if answer.lower() == 'no':
        num1 = ''
    if answer.lower() == 'quit':
        print('Exiting calculator...')
        calculating = False

# TODO: Use the dictionary operations to perform the calculations

# asks if the user wants to continue
# if yes, loop using the previous result as the first number and repeat (while loop)
# if no, restart with clearing the number