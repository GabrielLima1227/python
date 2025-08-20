# Accessing and Modifying Data:
# 1. The tarditional way: Make the data private and use Getters and Setters:

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email

    def set_email(self, email) -> None:
        self._email = email
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
print(user01._email) # Estado de protegido é apenas uma convenção em Python. Podemos Acessa-lo fora da classe da mesma forma. 
print(user01.clean_email())

user02 = User("batman", "bat@outlook.com", "456")
user01.say_hi_to_user(user02)