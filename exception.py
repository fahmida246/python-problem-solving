try:
    age = int(input("age:"))
except:
    print("you didn't enter valid stuff")
else:
    print("no exception")
print("execution continues")

# file close in exceptions
# try:
#     file = open("app.py")
#     age = int(input("age: "))
#     xfactor = 10/age
# except:
#     print("you didnt enter valid age")
# finally:
#     file.close()
#

# better way
try:
    with open("app.py") as file:
        print("file opened")
    age = int(input("age:"))
    xfactor = 10/age
except:
    print("you didnt enter valid score")
else:
    print("continue..")
