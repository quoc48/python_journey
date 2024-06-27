import random

def roll_die():
    """Simulates rolling two six-sided dice and returns the total."""
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    return total

print("Let's roll the dice!")
result = roll_die()
print("You rolled a total of:", result)
