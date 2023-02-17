# dictionary onordered cant be sorted so list is important
point = {'x': 1, 'y': 2}
point1 = dict(x=1, y=2)

point['x'] = 10
point['z'] = 20
print(point)
print(point1)

if 'a' in point:
    print(point["a"])

print(point.get('a'))

del point['x']
print(point)

for x in point:
    print(x, point[x])

for key, value in point.items():
    print(key, value)

# use of comprehensions
values = []
for x in range(5):
    values.append(x*2)

print(values)

comp = [x*2 for x in range(5)]
print(comp)

mapi = list(map(lambda x: x*2, range(5)))
print(mapi)

# dictionary comprehension

values = {}
for x in range(5):
    values[x] = x * 2
print(values)

values = {x: x*2 for x in range(5)}
print(values)

# unpacking operator list
first = [1, 2]
second = [3, 4]
values = [*first, 1, *second]
print(values)

# unpacking operator dictionary
first = {'x': 1}
second = {'y': 2}
result = {**first, **second, 'z': 6}
print(result)
