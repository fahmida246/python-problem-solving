# set is unordered
num = [1, 1, 2, 3, 4]
first = set(num)
second = {1, 5}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")
