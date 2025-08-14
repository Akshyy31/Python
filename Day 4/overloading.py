class Maths :
    def add(self,*args):
        result=0
        for i in args:
            result+=i
            
        return result
    
    
s1=Maths()
print(s1.add(1,2,3))
print(s1.add(1,2,3,4,6))
print(s1.add(1,2,3,4,6,7,8,9,10))