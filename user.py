class User:
    """Onboarding new user."""

    def __init__(self, first_name, last_name, user_age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n--- User information ---")
        print(f"- First name: {self.first_name.title()}")
        print(f"- Last name: {self.last_name.title()}")
        print(f"- Age: {self.user_age}")

    def greet_user(self):
        print(f"Wellcome {self.first_name.title()} {self.last_name.title()} to the team!")

    def login_attempt(self):
        print(f"Login attempts: {self.login_attempts}")

    def increase_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempt(self):
        self.login_attempts = 0



