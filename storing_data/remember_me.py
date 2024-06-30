from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists() and path.stat().st_size > 0:
        contents = path.read_text()
        user_profile = json.loads(contents)
        return user_profile
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    user_profile = {}
    user_profile['username'] = input("What's your name? ")
    user_profile['age'] = input("How old are you? ")
    user_profile['major'] = input("What is your major? ")
    contents = json.dumps(user_profile)
    path.write_text(contents)
    return user_profile

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_profile = get_stored_username(path)
    confirm = input(f"You are {user_profile['username']}? (y/n)")
    if user_profile and confirm.lower() == 'y':
        print("\nWelcome back!")
        for key, value in user_profile.items():
            print(f"- {key}: {value}")
    else:
        user_profile = get_new_username(path)
        print(f"We'll remember you when you come back, {user_profile['username']}.")

greet_user()