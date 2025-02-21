class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return f"Privet, меня зовут {self.name}, moi lvl {self.lvl}, moi hp {self.hp}"

    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False

superman = Hero('Rob', 12, 210)
print(superman.introduce())

ironman = Hero("Tony", 8, 200)
halk = Hero("john", 12, 200)
print(ironman.is_adult())
print(halk.is_adult())















