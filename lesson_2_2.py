

class Games:
    def __init__(self, game_name, graphics, adjuster, location):
        self.game_name = game_name
        self.graphics = graphics
        self.adjuster = adjuster
        self.location = location


    def info_about_game(self):
        print(f"Game - {self.game_name}, {self.graphics}, {self.adjuster}, {self.location}")

    def start_game(self):
        pass


    

class Maincraft(Games): 
    def __init__(self, game_name, graphics, adjuster, location):
        # super().__init__(game_name, graphics, adjuster, location)
        Games.__init__(self, game_name, graphics, adjuster, location)
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

    def start_game(self):
        print("Maincraft запустился и готов к игре")

main = Maincraft("maincraft", "ultra", "hard", "field")
main.info()
main.info_about_game()

class Roblox(Maincraft): 
    def __init__(self, name, pol, skin, hight):
        self.name = name
        self.pol = pol
        self.skin = skin
        self.health = 10
        self.hight = hight

    def info(self):
        print(f"персонаж - {self.name}, {self.pol}, {self.skin}, {self.health}, {self.hight}")

    def start_game(self):
        print("Roblox запустился и готов к игре")

rob = Roblox("Test", "woman", "back", 160)
# rob.edit_player()
rob.info()


main.start_game()
rob.start_game()



class Animals:
    def make_sound(self):
        pass


class Cow(Animals):
    def make_sound(self):
        print("MOO-MOO")


class Dog(Animals):
    def make_sound(self):
        print("Gaf-Gaf")


class Cat(Animals):
    def make_sound(self):
        print("Meow")


cow = Cow()
dog = Dog()
cat = Cat()

cat.make_sound()
dog.make_sound()
cow.make_sound()





