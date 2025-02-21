import sqlite3

connect = sqlite3.connect('../User.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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

#
# add_user("John", 33, "plavanie")
# add_user("Ardager", 25, "begat")
# add_user("Max", 30, "spat")
# add_user("Ilon", 18, "nichego")

# def get_all_users():
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     print(users)
#     print('Spisok vseh polzovatelei')
#
#     for i in users:
#         print(f'NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}')



def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchall()
    print(f'name: {name}, age: {user[0][2]}, hobby: {user[0][3]}')

get_user_by_name("Ardager")
get_user_by_name("John")

