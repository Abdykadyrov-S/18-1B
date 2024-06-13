
class Car:
    wheels = 4
    door = 4
    win = 6 
    def __init__(self, brand, max_speed, year):
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        self.is_start = False
        self.fuel_tank = 0

    def info_about_car(self):
        print(f"Марка машины - {self.brand}, {self.max_speed}, {self.year}")
        print(f"кол-во колес - {self.wheels}, {self.door}, {self.win}\n")

    def start(self):
        if self.fuel_tank > 0:
            self.is_start = True
            print(f"машина {self.brand} завелась")
        else:
            print("Нет бензина!")

    def drive(self, a):
        if self.is_start == True:
            print(f"Машина {self.brand} едет в {a}")
        else:
            print("Машина не завелась")

    
    def stop(self):
        if self.is_start == True:
            self.is_start = False
            print(f"машина {self.brand} заглушена")
        else:
            print("Машина не заводилась")

    def fill(self, value):
        self.fuel_tank += value
        # self.fuel_tank = self.fuel_tank + value

bmw = Car("bmw - m5", 360, 2022)
bmw.info_about_car()

mers = Car("mers - CLS", 400, 2005)
mers.info_about_car()

bmw.fill(20)
mers.fill(50)

bmw.start()
mers.start()

bmw.drive("Бишкек")
mers.drive("Geeks")


bmw.stop()
mers.stop() 



class Maincraft:
    def __init__(self):
        self.name = "player" 
        self.pol = "man" 
        self.skin = "Stiv"
        self.health = 10
    
    def info(self):
        print(f"персонаж - {self.name}, {self.pol}, {self.skin}, {self.health}")

    def edit_player(self):
        name = input("Введите имя персонажа: ")
        pol = input("Выберите пол персонажа: ")
        skin = input("Выберите скин персонажа: ")
        self.name = name 
        self.pol = pol
        self.skin = skin 


main = Maincraft()
main.info()
main.edit_player()
main.info()

    