class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old and I am {self.gender}")

p1 = Person("Derrick", 24, "male")
print(p1)

p1.introduce()
