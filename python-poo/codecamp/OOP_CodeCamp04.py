# Accessing and Modifying Data:
# 1. The tarditional way: Make the data private and use Getters and Setters:

from datetime import datetime

# Name Mangled
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        print(f"Email accesssed at {datetime.now()}")
        return self._email

    def set_email(self, new_email) -> None:
        self._email = new_email
        return self._email

    def clean_email(self) -> None:
        return self._email.lower().strip()

    def say_hi_to_user(self, user):
        print(
            f"Sending Message to {user.username}. Hi {user.username}, it's {self.username}"
        )

# Test
user01 = User("danthemna", "Dan@gmail.com ", "123")
print(user01.get_email())
print(user01.clean_email())
print(user01.set_email("Danthemna@gmail.com"))
print(user01.clean_email())

user02 = User("batman", "bat@outlook.com", "456")
user01.say_hi_to_user(user02) 