# # memory location
# # mutable and immutable
# # example of immutable
# x = 1
# print(id(x))

# x = x+1
# print(id(x))

# # example of mutable
# y = [1, 2, 3]
# print(id(y))

# y.append(4)
# print(id(y))
# # string

# s1 = "something"
# print(s1)
# print(s1[0])
# print(s1[1:2])

# # escaping
# # \ "
# # \ '
# # \\
# # \n

# # formated string
# first = "first"
# last = "last"
# full = first + " " + last
# print(full)

# first = "first"
# last = "last"
# full1 = f"{first}{2+2}"
# print(full1)

# # string method
# course = "python programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print("programming" in course)
# print(course.find("pro"))
# print(course.replace("pr", "_"))

# # ternary operator
# age = 17
# if age > 18:
#     msg = "greater than 18"
# else:
#     msg = "less than 18"

# msg1 = "greater than 18 " if age > 18 else "less than 18"


# print(msg)
# print(msg1)

# # for loop

# for x in "python":
#     print(x)

# for x in range(1, 5):
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

# print(type(range(1000)))

# for else
names = ['john', 'mary', 'mark']
found = False
for name in names:
    if name.startswith("j"):
        print("found")
        found = True
        break
if not found:
    print("not found")


# another type for else
names = ['ajohn', 'mary', 'mark']
for name in names:
    if name.startswith("j"):
        print("found")
        break
else:
    print("not found")

# functions


# def incre(num, by=1):
#     return (num, num+by)


# print(incre(2))

def incre(num: int, b: int = 1) -> int:
    return num+b


print(incre(2))

# xargs : for tuple


def multi(*tuple):
    total = 1
    for tup in tuple:
        total *= tup
    return total


print(multi(2, 3, 4, 5))

# xargs : for tuple


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="adam")
