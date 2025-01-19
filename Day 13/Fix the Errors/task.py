try:
    age = int(input("How old are you?"))
except ValueError:
    print('The input was not a number. Please enter a number.\n')
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")


