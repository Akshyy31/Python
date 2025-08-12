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

Empty = []

Empty.append(10)
Empty.extend([20,30,40,50])
Empty.insert(1,{"id":1})
print(Empty)
print(len(Empty))