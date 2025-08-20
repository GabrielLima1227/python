# Static Attribute

# A static attribute (sometimes called a class attribute) is an attribute that belongs to the class itself, not to any specific instance of the class.

class User:
    # Statical attributes are useful, for example, for tracking the number, Constants and settings of objects created.
    user_count = 0
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
    
    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user01 = User("MajinBoo", "MajinBoo@gmail.com")
user01.display_user()

print("-=" * 25)

user02 = User("Babidi", "Babidi@gmail.com")
user02.display_user()

print("-=" * 25)

print(User.user_count)
print(user01.user_count)
print(user02.user_count) 