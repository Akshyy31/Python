# range

# R = range(8)
# print(R)
# print(type(R))
# print(R[-1])

# R = range (5,16,2)

# for i in R:
#     print(i)

# r =  (range(20))
# print(r)
# print(type(r))
# for i in r:
#     print(i)

# mytuple = (1,2,3,4,"Akshay")
# print(mytuple[-1])
  
# change tuple value using list  

# myTuple = (2,3,4,5,6,7,8,9)
# myList = list(myTuple)
# myList.append(10)
# myTuple=tuple(myList)
# print(myTuple)


my_tuple = (10, 20, 30)
temp_list = list(my_tuple)
temp_list[2] = 99  # Change value
my_tuple = tuple(temp_list)
print(my_tuple)  