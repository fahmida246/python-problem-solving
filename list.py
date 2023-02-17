from collections import deque
letters = ['a', 'b', 'c']
matrix = [[1, 2, 3], [4, 5, 6]]
zeros = [0]*5
combined = zeros+letters
numbers = list(range(20))
chars = list("hi")
print(len(chars))
print(chars)

# list unpacking
num = [1, 2, 3, 4, 4, 5, 6]
first, *other, last = num
print(first)
print(last)

# loop over list
letters = ['a', 'b', 'c', 'd']
# items = (0,'a')
# index,letter = items
for index, letter in enumerate(letters):
    print(index, letter)

# adding or removing items
letters = ['a', 'b', 'c', 'd']
# add
letters.append('d')
letters.insert(4, 'j')
# remove
letters.pop(0)
letters.remove('b')
del letters[0:3]

print(letters)

# finding items
letters = ['a', 'b', 'c', 'd']
print(letters.count('b'))
if 'd' in letters:
    print(letters.index('d'))

# sorting list
numbers = [3, 4, 5, 67]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
# tuple sort
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# sort using lambda function
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
items.sort(key=lambda item: item[1])
print(items)

# map function / convert list of tuples to list
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
prices = []
for item in items:
    prices.append(item[1])

print(prices)
# alternate map
pri = list(map(lambda item: item[1], items))
print(pri)
# alternate list comprehesion
pri1 = [item[1] for item in items]
print(pri1)
# filter

x = list(filter(lambda item: item[1] >= 10, items))
print(x)
# alternate list comprehesion
x1 = [item[1] for item in items if item[1] >= 10]
print(x1)

# alternate
filter = []
for item in items:
    if item[1] >= 10:
        filter.append(item[1])
print(filter)

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))
print(list(zip('abc', list1, list2)))

# stack
browsing_session = []
browsing_session.append(1)  # insert
browsing_session.pop()    # delete
# if not browsing_session:
#     browsing_session[-1]

# queue
que = deque([])
que.append(1)
que.append(2)
que.popleft()
print(que)

