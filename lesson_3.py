" Инкапсуляция "


class Phone:
    def __init__(self, brand, password, gallery):
        self.brand = brand # Публичный
        self._password = password # Защищенный
        self.__gallery = gallery # Приватный 

    "@ - декоратор"
    @property
    def gallery(self):
        return self.__gallery

    def info(self):
        print(f"Модель телефона - {self.brand}\nПароль - {self._password}")
        self.__private()

    def info_about_protected(self):
        self._protected()

    def _protected(self):
        print("Secuirity info")
        self.__private()

    def __private(self):
        print("Private info")

    def main(self):
        while True:
            print("Выберите метод который хотите щзапустить: ")
            method = int(input("1-info, 2-protected, 3-private\n:"))
            if method == 1:
                self.info()
            elif method == 2:
                self._protected()
            elif method == 3:
                self.__private()
            else:
                break
        
    @property
    def private(self):
        return self.__private
    

passwords = [1234, 9999, 0.001, "qwerty"]
phone = Phone("iphone", passwords, "Галерея")
print(phone)

# phone.main()

# phone.info()

# print(phone.brand)
# phone.brand = "Samsung"
# print(phone.brand)
# print(phone.gallery)

# phone.private()
# phone.info_about_protected()



# print(phone.brand)
# print(phone._password)



# phone._protected()

# " декортаор - @ "


# def greet(value):
#     def start():
#         print("Hello!")
#         value()
#         print("Bye!")
#     return start







# @greet
# def result():
#     print(2+2)

# result()


