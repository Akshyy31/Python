
def greet_decor(fun):
    def Wrapper():
        print("Welocome Akshay")
        fun()
        print("Bye Bye")        
    return Wrapper
 
# @greet_decor        #  new way /  easy way to call decorator
def greet():
    print("hello Akshay")
        
# modFun = greet_decor(greet)   #normal way to call the function using clousure logic
# modFun()

# Count Function Calls
# Create a decorator count_calls that:
# Keeps track of how many times a function is called.
# Prints the count each time.
# # Apply it to a function say_hello(name).

# def count_calls(fun):
#     count=0
#     def wrapper(n):     
#         nonlocal count
#         count+=1
#         result=fun(n)
#         print(count)
#         return result   
#     return wrapper
    

# @count_calls
# def say_hello(name):
#     print(f"calls count {name} ")

# say_hello("akshay")
# say_hello("akshay")
# say_hello("akshay")


# class Decorator

# def add_start_method(cls):
#     def start(self):
#         print(f"{self.color} car Started")    
#     cls.start=start
#     return cls


# @add_start_method
# class Cars:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
        
#     def stop(self):
#         print(f"{self.name} car was stopped")

# c1=Cars("Audi","Black")

# c1.stop()
# c1.start()

# Common built in decorator 
# staticmethod 
# class Maths:
#     @staticmethod
#     def sum(a,b):
#         return b+a

# print(Maths.sum(10,20))

# @classmethod 

class Maths:
    count=10
    # @classmethod
    def sum(self):
         self.count +=  1 
         return self.count 


s=Maths()
print(s.sum())
print(s.sum())
print(s.sum())


print(Maths.count)
print(Maths.count)
print(Maths.count)


class Maths:
    count=10
    @classmethod
    def sum(cls):
         cls.count +=  1 
         return cls.count 


print(Maths.sum())
print(Maths.sum())
print(Maths.sum())




print(Maths.count)
print(Maths.count)
print(Maths.count)
