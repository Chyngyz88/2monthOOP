# Декораторы, logi4eskie metody


# def my_decorator(func): # 2
#
#     def wrapper():
#         print('перед выполнением функции') # 4
#         func() # 5
#         print('после выполнения функции') # 6
#
#     return wrapper # 3
#
# @my_decorator
# def hello():
#     print("привет мир!!")
#
# hello() # 1
#
# # Dekoratory s argumentami
#
# def repeat(n): # 2
#
#     def decorator(func): # 4
#
#         def wrapper(*args, **kwargs):
#             for i in range(n): # 6
#                 func(*args, **kwargs) # 6
#
#             return wrapper # 5
#         return decorator
#
#
# # @repeat(3)
# def greet():
#     print("Privet!!")
#
# greet() # 1
#
# # Dekoratory dlya klassa
#
# def class_decorator(cls):
#
#     class NewClass(cls):
#
#         def new_method(self):
#             return print("Noviy metod!!")
#
#     return NewClass
#
# @class_decorator
# class MyClass:
#
#     def old_method(self):
#         return print("Stariy metod")
#
# obj = MyClass()
# obj.old_method()
# obj.new_method()
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self,):
#         return f'dvlkdvl'
#
#
# # obj = Person("Pavel", 25)
# #
# # print(obj)
#
# class Money:
#
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __add__(self, other):
#         return Money(self.amount + other.amount)
#
#     def __str__(self,):
#         return f"{self.amount} som"
#
#     def __len__(self):
#         return f"pass"
#
#     def __call__(self, news_view_):
#
# m1 = Money(100)
# m2 = Money(100)
# m3 = m1 + m2
# len(m3)

class Math:

    @staticmethod
    def add(a, b):
        return a + b

obj3 = Math()

print(obj3.add(1,2))

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    @classmethod
    def create_person(cls, name):
        return cls(name)

person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Bobs")
print(Person.get_population())
person4 = Person.create_person("john")
print(person4.name)






















