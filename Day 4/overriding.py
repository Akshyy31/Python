
class Animal:
    def sound(self):
        return ("Animal make sound")
        
        
class Dog(Animal):
    def sound(self):
        return ("Dog make sound")
        
        
class Crow(Animal):
    def sound(self):
        return("crow make sound")
        
        
c=Crow()
d=Dog()
a=Animal()
print(c.sound())
print(d.sound())
print(a.sound())