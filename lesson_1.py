" Объектно-ориентированное программирование (ООП) "

# mega_super_home = 23

# MegaSuperHome = 34 


class Home: # чертеж или же шаблон
    door = 2 # Атрибут/поле (свойства) класса 
    "init - конструктор" 
    "self = ссылка на текущий объект (сам объект)" 
    def __init__(self, win):
        self.win = win # Атрибут/поле (свойства) объекта

    def info(self):
        print(f"Кол-во окон в доме {self.win}, кол-во дверей {self.door}")


home = Home(1)
home_2 = Home(5)
home_3 = Home(6)


home.info()

# print(home.win, home.door)
# print(home_2.win, home_2.door)
# print(home_3.win, home_3.door)


