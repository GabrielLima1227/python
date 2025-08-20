class User:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.__email = email
        self.password = password

    @property
    def email(self):
        print("Email Accessed")
        return self.__email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email


user01 = User("dantheman", "dan@gmail.com", "123")
user01.email = "MajinBoo@hotmail.com"
print(user01.email)