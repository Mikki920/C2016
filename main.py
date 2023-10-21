class Student:
    group = "C2016"

    def __init__(self, age, height, name):
        self.name = name
        self.age = age
        self.height = height
        print("Обьект был создан")


    def __str__(self):
        return f"I'm name {self.name}


nick = Student(16, 165, "Nick")
print(nick.age)
print(nick.height)
print(nick.name)


Kate = Student(18, 163, "Ekaterina")
print(Kate.age)
print(Kate.height)
print(Kate.name)
