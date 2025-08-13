
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
# Apply it to a function say_hello(name).

def count_calls(fun):
    count=0
    def wrapper(n):     
        nonlocal count
        count+=1
        result=fun(n)
        print(count)
        return result   
    return wrapper
    

@count_calls
def say_hello(name):
    print(f"calls count {name} ")

say_hello("akshay")
say_hello("akshay")
say_hello("akshay")