d= dict([("a","akshay"),("A","shaym"),( 1,123 )])
# d= dict(a="akshay",A="shaym", 1 = 123 )

# print(d)
# print(d["a"])

# myTuple = ("akshay",)
# print(type(myTuple))

dic= {"name":"Akshay","age":23,"place":"Vtk"}
dic["height"]=169        # add key value using =
dic["weight"]=65

dic["weight"]=62         # update
dic["name"]="Akshay shaji"

# del dic["weight"]        # delete value using del keyword
# ret=dic.pop("name")      # rmove the item by using key and return the deleted value
# dic.clear()            # remove all items in the dictionary

# key,value= dic.popitem()
# print(f"key :{key}  value : {value} ")
# print(dic)
# print(ret)

# for i in dic.keys():
#     print(i)

# for i in dic.values():
#     print(i)
    
# for i , j in dic.items():
#     print(i, "   ",j)

# import copy
# school = {"sname":"PKG","loc":"Kannur","pin":673103,"students":{ "id" : 1, "name":"sreya", "batch":"cs" }}


# # duplicate = school.copy()
# duplicate=copy.copy(school)
# duplicate1=copy.deepcopy(school)


# duplicate["students"]["deprt"]="IT"
# duplicate["place"]="pinaray"


# print("duplicate : ",duplicate)
# print("duplicate : ",duplicate1)
# print("Original  : ",school)

# rollNo=[1,2,3,4]
# name=["akshay","shyam","vinayak","Sam"]

# students= zip(rollNo,name)
# print(students)
# print(dict(students))

# dictionary comprehension 

# prices = {"Apple":160,"kiwi":180,"Orange":80}

# updated_price = {key : value+50 for key,value in prices.items()}

# print(updated_price)

# lists={i: i*10 for i in range(1,10)}
# print(lists)


# even = {i: i*i for i in range (20) if i*i%2==0 }
# print(even)

# person1 = {"name": "Akshay", "age": 25, "city": "Pune"}
# news=tuple(person.items())
# print(news)
# print(type(news))

# person2={"name": "sree", "age": 29, "city": "Mumbai"}

# person1.update(person2)

# print(person1)
# print(person2)

# mytuple=(1,2,3,4,5)

# newdic= dict.fromkeys(mytuple)

# print(newdic)

# obj = {id:1,"name":"akshya","place":"vtk"}
# i need to change the old key name to new key full name 

# obj["full name"]=obj.pop("name")
# # new key                  #old key
# print(obj)

