class Point:
    def draw(self):
        print("draw some")


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))

# constructor

# class vs instance attribute


class Point:
    default_color = "yellow"  # class attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point({self.x})")


point = Point(1, 2)
point.z = 10  # instance attribute
print(point.z)
print(point.default_color)
point.draw()

another = Point(3, 4)
print(Point.default_color)
print(point.default_color)
point.draw()

# class attribute ja shob object use korte parbe
# instace attribute khali oi instace ba object use korte parbe

# compare object magic methods


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

point1 = Point(10, 20)
other1 = Point(1, 2)
print(point1 > other1)

# performing arithmetic operations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
comb = point + other
print(comb.x)

# custom container


class Cloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = Cloud()
len(cloud)
cloud.add("python")
len(cloud)
print(cloud.tags)

# inheritance


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


ani1 = Mamal()
print(ani1.age)
ani1.eat()
# 3
# getter,setter for private attribute, pproperties


class Product:
    def __init__(self, price):
        self.__set_price(price)

    def __get_price(self):
        return self.__price

    def __set_price(self, price):
        if price < 0:
            raise ValueError("price can not negetive")
        self.__price = price
    price = property(__get_price, __set_price)


product = Product(-50)
product.price = -1
print(product.price)

##


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price can not negetive")
        self.__price = price


product = Product(-50)
print(product.price)
