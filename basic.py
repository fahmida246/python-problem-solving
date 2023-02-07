# memory location
# mutable and immutable
# example of immutable
x = 1
print(id(x))

x = x+1
print(id(x))

# example of mutable
y = [1, 2, 3]
print(id(y))

y.append(4)
print(id(y))
# string

s1 = "something"
print(s1)
print(s1[0])
print(s1[1:2])

# escaping
# \ "
# \ '
# \\
# \n

# formated string
first = "first"
last = "last"
full = first + " " + last
print(full)

first = "first"
last = "last"
full1 = f"{first}{2+2}"
print(full1)

# string method
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print("programming" in course)
print(course.find("pro"))
print(course.replace("pr", "_"))
