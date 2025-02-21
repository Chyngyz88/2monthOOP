from faker import Faker

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduce(self):
        return f"Hello, my name is {self.name}, my address: {self.address}"
fake = Faker()
student1 = Student(fake.name(), fake.address())
print(student1.introduce())


"""Eta biblioteka ispolzuetsia dlia sozdania faikov
dannyh chtoby testit ili zapolniat bazu dannyh"""





















