class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\n--- The user's set of privileges ---")
        for privilege in self.privileges:
            print(f"- {privilege}")