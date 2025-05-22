class Person:


    def __init__(self, name, id, color, add):
        print("This is a parameterized constructor")
        self.name = name
        self.id = id
        self.color = color
        self.add = add

    def Talk(self):
        print("Who is talking--->" +self.name)

    def walk(self):
        print("Who is Walking--->" +self.name)


# Creating an object for the above class

Person1 = Person("rogger1", 34, "white", "Delhi")
print(Person1.name, Person1.color, Person1.id, Person1.add)
Person1.Talk()
Person1.walk()

Person2 = Person("rogger2", 344, "Fair", "Mumbai")
print(Person2.name, Person2.color, Person2.id,Person2.add)
Person2.walk()
Person2.Talk()
