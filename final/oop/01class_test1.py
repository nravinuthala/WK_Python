class Person:
    '''
    This class defines the blueprint of a person and can be used to create person instances.
    '''

    def __init__(self, pname, age):
        self.__pname = pname
        self._age = age

    def greet(self):
        print(f"Hello {self.__pname}")


#
p1 = Person("Nagaraj", 45)
p2 = Person("Ravi", 40)
# p1.greet()
# # Person.greet(p1, "Ravinuthala")
#
# # print(Person.pname)
# # print(Person.age)
#
# print(p1.pname)
# print(p1.age)

# print(p1.__pname)
print(hasattr(p1, "_Person__pname"))
# print(getattr(p1, "__pname"))
setattr(p1, "__pname", "Ravi")
print(getattr(p1, "__pname"))
# delattr(p1, "__pname")
print(p1.__dict__)




# built in class methods
#
# print(getattr(p1, "pname"))
# setattr(p1, 'pname', "Ravinuthala")
# print(getattr(p1, "pname"))
# print(getattr(p1, "p_name"))

# print(hasattr(p1, "pname"))
# print(hasattr(p1, "p_name"))
#
# print(hasattr(p1, "age"))
# delattr(p1, 'age')
# print(hasattr(p1, "age"))
#
#
# # # # built in class attributes
# # print(p1.__doc__)
# print(p1.__dict__)
#
# # print(p1.__class__)
# # print(p1.__module__)
# # print(p1.__bases__)
# del p1.age
# # del p1.greet()
# print(p1.__dict__)
# print(p2.__dict__)