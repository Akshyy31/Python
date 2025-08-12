# What is a Lambda Function?
# A lambda function is a small, anonymous (unnamed) function in Python.
# Created using the lambda keyword.
# Can have any number of parameters, but only one expression (no multiple statements).
# Returns the result of that expression automatically.


# lambda argumets : expresion 



# ckeck the number is positive or not 

# check = lambda res :  print("positive num") if res>0  else print("negative number") if res < 0 else print("Zero")

# check(-1)


# def add (a,b):
#     return a+b
# print(add(10,20))

# add = lambda a,b :a+b
# print(add(100,200))

# lambda with list comprehension 

# nums = [1, 2, 3, 4, 5]
# square = lambda n : n*10
# newlist =[square(n) for n in nums ]
# print(newlist)

# ten = lambda x : x*10
# li = [ten(i) for i in range(1,11)]
# print(li)

# for i in li :
#     print(i*10)
    
# The lambda function squares each element.
# The list comprehension iterates through li and applies the lambda to each element.
# This is ideal for applying transformations to datasets in data preprocessing or manipulation tasks.

# Q1 Given a list of numbers, create a new list containing the squares of each number. 

# nums=[1,2,3,4,5,6,7,8]
# square=lambda x: x**2
# lists= [square(i) for i in nums]
# print(lists)

# Q2 Given a list of numbers, return a list that says "even" or "odd" for each number.

# nums=[1,2,3,4,5,6,7,8,9]
# fn=lambda x:"even" if x%2==0 else "odd" 
# newlist = [fn(i) for i in nums]
# print(newlist)

# Q3 Given a list of strings, create a list of their lengths. 

# str=["Akshay","shyam","vinayak","samadev"]
# length = lambda s  : len(s)

# newlist = [length(i) for i in str ]
# print(newlist)

# Q 4 Given a list of names, return a list where each name is capitalized (first letter uppercase).
# names=["akshay","shyam","vinayak","samadev"]
# newlist =[(lambda s: s.capitalize())(i) for i in names]
# print(newlist)

# lambda with multiple statement 

# res = lambda a,b :((a+b), (a-b))
# print(res(100,50))

# filter,map,reduce  and lambda
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
res=filter(lambda x: x%3==0 , nums)
resMap=map(lambda i : i**2 , nums)
resRed=reduce(lambda x,y:x+y,nums)
print(list(res))
print(list(resMap))
print(resRed)