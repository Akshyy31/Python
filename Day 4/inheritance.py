# class Peroson:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def display(self):
#         print(f"name is {self.name}   ,  age is {self.age} ")

# class Employee(Peroson):
    
#     def print(self):
#         print("employee class (child) class called")
        
        

# e1=Employee("Samadev",45)
# e1.display()
# e1.print()


# super()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
        
#     def display(self):
#         print(f"name : {self.name}")
#         print(f"age : {self.age}")
        

# class Employe(Person):

#     def __init__(self, name, age,salary,place):
#         super().__init__(name, age)
        
#         self.salary=salary
#         self.place=place
        
#     def display(self):
#         super().display()
#         print(f"slaray : {self.salary}")
#         print(f"place : {self.place}")
    
    
# e1=Employe("Kahsy",23,1000000,"vtk")

# e1.display()

# multiple inheritance 

class parent1:
    def show(self):
        print("parent 1")
    
class Parent2:
    def show(self):
        print("parent 2")
    
class Child(parent1,Parent2):
    def show(self):
        print("Child of both")     
        super().show()
    pass
        
c1=Child()
c1.show()

# print(c1.__mro__)