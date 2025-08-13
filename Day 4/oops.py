# Class

# A class in Python is a user-defined template for creating objects.
# It bundles data and functions together, making it easier to manage and use them.
# When we create a new class, we define a new type of object. We can then create multiple instances of this object type

# Classes are created using class keyword. Attributes are variables defined inside the class and represent the properties of the class.
# Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).


# Object

# An object is a specific instance of a class. It holds its own set of data (instance variables) and can invoke the methods defined by its class.
# Multiple objects can be created from the same class, each with its own unique attributes.

# init() 

# __init__() is not mandatory — if you don’t define it, Python uses a default one.
# It’s like a constructor in other languages (Java, C++).
# self lets you store data in the object (as attributes).
# Runs only once per object at creation time.



class Cars: 
    def __init__(self,n,p,c):
        self.name=n
        self.price=p
        self.colour=c
    
    def start(self):
        print(f"{self.name} car was started")
        
    def stop(self):
        print(f"{self.colour} car was stopped")
        
        
car1=Cars("Audi",100000,"black")

car1.name="Benz"

car1.start()
car1.stop()
    