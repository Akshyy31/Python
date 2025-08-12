# def greet():
#     print("Welocome Python")   
# greet()

# Arguments

# def check(num):
#      return "Even" if num % 2 == 0 else  "odd" 
# print(check(6))
# print(check(5))

# default argument 

# def greet(name="Akshay"):
#     print(f"hello {name}")
# greet()
# greet("Akshay shaji")
# def sum(num2, num1=100, num3=300):
#     print(num1)
#     print(num2)
#     print(num3)
#     print(num1+num2+num3)  
# sum(300, 200, 500)

# keyword argument 

# def Details(name,age):
#     print(f"name is {name}")
#     print(f"Age is {age}")
    
# Details(age=45,name="akshay")

# Arbitary Argument 

# def sum(*nums):
#     total=0
#     for i in nums:
#         total+=i
#     return total

# print(sum(1,2,3,4,5,6,7,8,9,10))
# print(sum(1,2,3,4,5))

# def names(fistname,lastname,*args):
#     print("firstname : ",fistname)
#     print("othernames  : ", args)
#     print("lastname  : ", lastname)
    
# names("Akshay","shaym","vinayak","samadev","aswin")


# kwargs

def details(*args,**kwargs):
    print(kwargs)
    print(args)
    for key , value in kwargs.items():
        print(f"{key}   : {value}")
    
details(1,2,3,name="vatakara")
    