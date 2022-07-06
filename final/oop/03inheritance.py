# import classes_objects
# print('hello')

from classes_objects import Person

class Teacher(Person):

    profession = "Teacher"
    def __init__(self, fn, ln):
        super().__init__(fn, ln)

bob = Teacher("Bob", "Dylan")
print(bob.profession)
print(bob.full_name())
print(bob.name())