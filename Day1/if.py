age =25
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("you are not eligible for vote")
    
# if age>=18:print("Eligible for vote")  # short syntax write in oneline

# if else 

# if age>=18:
#     print("Eligible for vote")
# else:
#     print("you are not eligible for vote")

# print("Eligible for vote") if age >=18 else print("Not eligible for vote")   # short syntax in one line
# number = 9
# print (f"Even {number}") if number%2==0 else print(f"Odd {number}") 

# elif 

# if age <= 12 :
#     print("Child")
# elif age<=18:
#     print("teenager")
# elif age<=30:
#     print("Young adult")
# else:
#     print("adult")

# nested if else 

# age=3
# is_valid=False

# if age>=18:
#     if is_valid:
#         print("login success")
#     else:
#         print("login unsuccesful")    
# else:
#     print("not eligible")

# match - case 
# command = "start"  # matching by value
# match command:
#     case "start":
#         print("greeeen")
#     case "stop":
#         print("red")
        
#     case _:
#         print("Warning")


# matching by datatypes 

# data = [5,"akshay"]

# match data:
#     case int():
#         print(f"{data} is a integer")
#     case float():
#         print(f"{data} is a float")
#     case tuple():
#         print(f"{data} is a tuple")
#     case list():
#         print(f"{data} is a list")
#     case _:
#         print(f"{data} is a not in the case")
        
# unpacking data structure

point = (3,5)
match point:
    case(0,y):
        print(f" y aaxis = {y}")
    case(x,y):
        print(f" y axis")
    case(5,y):
        print(f" y")
    case _:
        print("no axis")