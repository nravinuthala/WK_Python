class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}")



p1 = Person("Nagaraj", 45)
p1.greet()
# Person.greet(p1, "Ravinuthala")

# print(Person.name)
# print(Person.age)

print(p1.name)
print(p1.age)
