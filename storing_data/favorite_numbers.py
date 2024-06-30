from pathlib import Path
import json


def write_favorite_number(path):
    """Ask user about unique favorite number input."""
    favorite_numbers = []
    while True:
        favorite_number = input("What is your favorite number? (or 'q' to quit): ")
        if favorite_number.lower() == 'q':
            break
        elif favorite_number not in set(favorite_numbers):
            favorite_numbers.append(favorite_number)
            content = json.dumps(favorite_numbers)
            path.write_text(content)
        else:
            print("The number entered already!")

def show_favorite_number(path):
    """Get stored favorite number."""
    favorite_number = path.read_text()
    content = json.loads(favorite_number)
    print(f"I know your favorite numbers! It's {content}.")

path = Path('favorite_numbers.json')
write_favorite_number(path)
show_favorite_number(path)