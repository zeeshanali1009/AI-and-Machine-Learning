# class Person:
#     name = "name"

#     def changename(self, name):
#         self.name = name

# p1 = Person()
# p1.changename("Zeeshan")
# print(p1.name)
# print(Person.name)
# it will not change the name of class attribute for changing the class attribute name as well we have to do the following thngs

# class Person:
#     name = "name"

#     def changename(self, name):
#         Person.name = name          # or self.__class__.name = "Zeeshan"

# p1 = Person()
# p1.changename("Zeeshan")
# print(p1.name)
# print(Person.name)
# this same work can also be done using the class methods easily

class Person:
    name = "name"

    @classmethod
    def changename(cls, name):
        cls.name = name
p1 = Person()
p1.changename("Zeeshan")
print(p1.name)
print(Person.name)


# so we have these three type of methods 
# static methods
# class methods (cls) 
# instance methods (self)

