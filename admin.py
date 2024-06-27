from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, user_age):
        super().__init__(first_name, last_name, user_age)
        self.privileges = Privileges('can add post', 'can delete post', 'can ban user')