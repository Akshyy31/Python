# def indent ():
#     print("indentation of this fn") 
#     print('outside fn')

# indent()
# if 8 < 12:
#     print("8 is smaller")
#     print("Comparison done")

# Write a program that:
# Checks if a number is positive.
# Inside that, check if it is greater than 10.
# Print a message for each condition.

def check (n):
    if(n%2==0):
        print("Number is positive")

        if(n>10):
            print("number is greater than 10")

check(18)
# Indent properly so the loop works as intended.
for i in range(3):
    print("Number:", i)
print("Done with iteration")

# Write a program that:
# Takes a username.
# If it’s "admin", print "Welcome, admin".
# Otherwise, print "Welcome, user".


def user(name,role):
    if(role=="admin"):
        print(f"Welocome {role}")
    else:
        print(f"Welcome {name}")

user("Akshay","")

# Write code using proper indentation so that the output is?
# Start
# Inside if
# Inside loop
# End

print ("start")
if True:
    print("inside if")
    for i in range(1):
        print("inside loop")
print("end")







