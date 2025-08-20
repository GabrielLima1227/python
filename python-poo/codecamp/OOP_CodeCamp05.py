class User:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.__email = email
        self.password = password

    @property
    def email(self):
        print("Email Accessed")
        return self.__email


user01 = User("dantheman", "dan@gmail.com", "123")
# user01.email = "This is not an email"
print(user01.email)