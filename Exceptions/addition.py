print("Give me two numbers!")
print("Enter q to quit.")

while True:
    number_1 = input("\nEnter first number: ")
    if number_1 == 'q':
        break
    try:
        number_1 = int(number_1)
    except ValueError:
        print("You have to enter a number!")

    number_2 = input("Enter second number: ")
    if number_2 == 'q':
        break
    try:
        number_2 = int(number_2)
    except ValueError:
        print("You have to enter a number!")