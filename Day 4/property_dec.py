
# class Person:
#     def __init__(self,name):
#         self.name=name
        
#     @property 
#     def getName(self):
#         return self.name
    
#     @getName.setter
#     def setName(self,value):
#         self.name=value
#         return self.name
    
    
# p1=Person("Akshay shaji")

# print(p1.getName)
# p1.name="Sreaya"
# print(p1.setName)
    
    
class FindRadius:
    def __init__(self,r:int):
        self.radius=r
    
    @property
    def diameter(self):
        diameter=self.radius*2
        return diameter
    @diameter.setter
    def setDiameter(self,newR):
        self.radius=newR
        newDia=self.radius*2
        return newDia
    
    
c1=FindRadius(6)

print(c1.diameter)
c1.radius=30
print(c1.setDiameter)
        
     