# tuple
p1 = 1, 2
print(type(p1))

p2 = (1, 2)+(3, 4)
print(p2)

p3 = (1, 2)*3
print(p3)

p4 = tuple("hello world")
print(p4)

# swap variable
x = 10
y = 11

x, y = y, x
print('x', x)
print('y', y)
