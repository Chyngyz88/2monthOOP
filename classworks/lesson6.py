# Множественное наследование

# Горизонтальное наследование
#
# class fly(self):
#     return 'Letit'
#
# class Swimmable:
#
#     def swim(self):
#         return  'Plavaet'
#
# class Duck(Flyable, Swimmable):
#
#     def make_sound(self):
#         return 'Kria-Kria!!'
#
# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())


#
# class Animal:
#
#     def make_sound(self):
#         return "Издает звук"
#
#     def action(self):
#         return 'Базовое действие'
#
#
# class Swimmable(Animal):
#
#     def action(self):
#         return 'Плавает'
#
#
# class Flyable(Animal):
#
#     def action(self):
#         return 'Летит'
#
#
# class Duck(Swimmable, Flyable):
#
#     def make_sound(self):
#         return 'Кря-Кря!!'
#
#     # def action(self):
#     #     return 'Летает и плавает'
#
#
# donald_duck = Duck()
# print(donald_duck.action())
# print(Duck.mro())


import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT   
    )
              ''')

connect.commit()


# CRUD - Create - Read - Update - Delete

# Create
def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, int(age), str(hobby))
    )
    connect.commit()
    print(f"Polzovatel {name} dobavlen")

# add_user("John", 33, "plavanie")
# add_user("Ardager", 25, "begat")
# add_user("Max", 30, "spat")
# add_user("Ilon", 18, "nichego")

def get_all_users():

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)
    print('Spisok vseh polzovatelei')

    for i in users:
        print(f'NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}')

        
get_all_users()









































































