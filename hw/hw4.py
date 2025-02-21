

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Vyzov funkcii {func.__name__} s argumentami: {args}")
        return func(*args, **kwargs)
    return wrapper()

@logger
def greet(name):
    print(f"Hello {name}!")

greet("Alice")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Priamougolnik {self.width}x{self.height}"

    def __add__(self, other):
        return f"{Rectangle(self.width + other.width, self.height + other.height)}"

rectangle1 = Rectangle(3,4)
rectangle2 = Rectangle(2,5)
rectangle3 = rectangle1 + rectangle2

print(rectangle1)
print(rectangle2)
print(rectangle3)






































