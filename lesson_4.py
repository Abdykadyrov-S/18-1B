" Магические методы - dunder методы "

class Work:
    def __init__(self, position, graphicks):
        self.position = position
        self.graphicks = graphicks

    def info(self):
        return 2 + 2
        # print(f"Позиция - {self.position}, график работы - {self.graphicks} это метод info")

    def __repr__(self): # print
        return f"Позиция - {self.position}, график работы - {self.graphicks} это __repr__"

    def __str__(self): # print
        return f"Позиция - {self.position}, график работы - {self.graphicks} это __str__"

    def __call__(self): # Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции
        print("Это Маг. метод __call__")


# teacher = Work("Backend Developer", "24/7")
# print(teacher)


# teacher()
# print(teacher.info())


class Math:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def __str__(self) -> str:
        return f"первое значение - {self.number_1} \nвторое значение - {self.number_2}"

    " Магические методы для арифметическмх действий "
    def __add__(self, other): # +
        """Создать новый объект как сумму координат 'self' и 'other'."""
        print(f"Результат сложения {self.number_1} и {other.number_1}")
        return Math(self.number_1 + other.number_1, self.number_2)

    def __sub__(self, other): # -
        print(f"Результат вычитания {self.number_1} и {other.number_1}")
        return Math(self.number_1 - other.number_1, self.number_2)
    
    def __mul__(self, other): # *
        print(f"Результат умножения {self.number_1} и {other.number_1}")
        return Math(self.number_1 * other.number_1, self.number_2)
    
    def __truediv__(self, other): # /
        print(f"Результат деления с остатком {self.number_1} и {other.number_1}")
        new_number_1 = self.number_1 / other.number_1
        return Math(new_number_1, self.number_2)

    def __floordiv__(self, other): # //
        print(f"Результат деления без остатком {self.number_1} и {other.number_1}")
        return self.number_1 // other.number_1
    

    " Магические методы для операторов сравнения "
    def __gt__(self, other): # >
        return self.number_1 > other.number_1
    
    def __lt__(self, other): # <
        return self.number_1 < other.number_1
    
    def __eq__(self, other): # ==
        return self.number_1 == other.number_1
    
    def __ne__(self, other): # !=
        return self.number_1 != other.number_1
    
    def __ge__(self, other): # >=
        return self.number_1 >= other.number_1
    
    def __le__(self, other): # <=
        return self.number_1 <= other.number_1

math_number_1 = int(input("Введите первое число: "))
math = Math(math_number_1, 2)


math_2_number_1 = int(input("Введите второе число: "))
math_2 = Math(math_2_number_1, 7)

print(math)
# print(math_2)

" Магические методы для арифметическмх действий "
# print(math + math_2)
# print(math - math_2)
# print(math * math_2)
# print(math / math_2)
# print(math // math_2)

" Магические методы для операторов сравнения "
print(math > math_2)
print(math < math_2)
print(math == math_2)
print(math != math_2)
print(math >= math_2)
print(math <= math_2)


