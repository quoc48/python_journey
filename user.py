class User:
    """Onboarding new user."""

    def __init__(self, first_name, last_name, user_age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age

    def describe_user(self):
        print(f"\n--- User information ---")
        print(f"- First name: {self.first_name.title()}")
        print(f"- Last name: {self.last_name.title()}")
        print(f"- Age: {self.user_age}")

    def greet_user(self):
        print(f"Wellcome {self.first_name.title()} {self.last_name.title()} to the team!")


user_1 = User('quoc', 'phan', 33)
user_2 = User('alex', 'Toan', 24)
user_1.describe_user()
user_2.describe_user()
print("\n--- Wellcome onboard ---")
user_1.greet_user()
user_2.greet_user()


