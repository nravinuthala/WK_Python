class Person:

    # class attribute
    species = "Human Being"

    def __init__(self, fname, lname): # , age, location, mobile):
        self.fname = fname
        self.lname = lname
        # self.age = age
        # self.location = location
        # self.mobile = mobile

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def name(self):
        return f'{self.lname}, {self.fname}'

john = Person("John", "Adams")
jessica = Person("Jessica", "Simpson")

print(Person.species)
print(john.species)
print(jessica.species)

print(john.full_name())
print(jessica.name())