class Sport:
    def __init__(self, type_sport):
        self.type_sport = type_sport

    def info(self):
        print("Это метод Info внутри класса Sport")

    def __str__(self):
        return f"Тип спорта {self.type_sport}"
    

class Voleyboll(Sport):
    
    def __str__(self):
        return super().__str__() + ' ' + "and Voleyball"


sport = Sport("Football")
# print(sport)
# sport.info()

# vol = Voleyboll("Voleyball")
# print(vol)
# # vol.info()


# a = "hi"
# b = "name"
# print(a + ' ' + b)

number = 3

number_2 = 4

if number < number_2:
    print(f"{number} < {number_2} First IF")
elif number < number_2:
    print(f"{number} < {number_2} Second IF")


