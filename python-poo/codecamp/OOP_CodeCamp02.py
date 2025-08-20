class Person:
    def __init__(self, name, age,) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person01 = Person("Alice", 20)
person01.greet()

person02 = Person("Gabriel", 20)
person02.greet()