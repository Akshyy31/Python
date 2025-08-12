# create list 

a=[10,"akshay",{"id":1},6,8,9,20]

# a = list((10,"akshay",{"id":1},6,8,9,20))
# dup = a.copy()

# a[2]["name"]="Bridgeon"

# print(a[0])
# print(a[-1])
# print(a)
# # print(dup)
# print(type(a))

# Empty = []

# Empty.append(10)
# Empty.extend([20,30,40,50])
# Empty.insert(1,{"id":1})
# print(Empty)
# print(len(Empty))

# remove 

arr =[ 1,2,3,4,5,6,7,8,9]

# arr.remove(5)
arr.pop(0)
print(arr)

# list comprehension 

squares = [ i**2 for i in range (1,11) if i%2==0]

# print(squares)

fruits =["appple","banana","kiwi"]
FRUITS = [i.upper() for i in fruits]
print(FRUITS)

# From range(1, 11), create a list of numbers divisible by both 2 and 3. 
lis=[i for i in range(1,11) if i%2==0 and i%3==0]
print(lis)

# Given sentence = "Python is fun", make a list of each character except spaces. 

str="Python is fun"
space =[ i for i in str if i!=" "]
print(space)

# From names = ["Akshay", "Shyam", "Aswin", "Vinayak"], create a list of names that start with the letter A. 

names = ["Akshay", "Shyam", "Aswin", "Vinayak"]
newname= [i for i in names if i.startswith("A")]
print(newname)

# From range(1, 21), create a list of "even" or "odd" strings depending on whether each number is even or odd. 

EV=["even" if i%2==0 else "odd" for i in range(1,21)]

print(EV)
