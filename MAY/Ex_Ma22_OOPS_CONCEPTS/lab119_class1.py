class Dog:
    name = None
    legs = None
    def wal(self):
        print("Walking")

    def sleep(self):
        print("Sleeping")

# Creating a reference or object of that class

dabar = Dog()

dabar.legs = 4
dabar.name = "Chottu"
dabar.sleep()
dabar.wal()
print(dabar.name)
print(dabar.legs)

# Object Ref
# Dog() - Object
# chow -> Object Ref.
mow = Dog() # creating a object for Dog class
bow = Dog() # creating a object for Dog class
rancho = Dog() # creating a object for Dog class

chow = Dog()  # creating a object for Dog class
chow.name= "ffsfdgf"
chow.wal()
chow.sleep()
chow.legs= 4
