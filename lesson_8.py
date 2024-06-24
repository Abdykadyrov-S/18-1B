import sqlite3

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        phone_number VARCHAR (15),
        age INT DEFAULT NULL,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        direction TEXT,
        rating DOUBLE (4,2) DEFAULT 0.0,
        birth_date DATE
        )""")


class GeeksStudents:
    def __init__(self):
        self.full_name = None
        self.phone_number = None
        self.age = 0
        self.is_have = False
        self.direction = None
        self.rating = 0.0
        self.birth_date = None


    def register(self):
        full_name = input("Введите ФИО: ")
        phone_number = int(input("Введите номер телефона: "))
        age = int(input("Введите возраст: "))
        is_have = bool(input("Наличие ноутбука: "))
        direction = input("Введите направление: ")
        birth_date = input("Введите дату рождения: ")

        cursor.execute(f"SELECT phone_number FROM students WHERE phone_number = {phone_number}")
        student = cursor.fetchone()

        if student:
            print("Already exists - Вы уже проходили регистрацию")

        else:
            cursor.execute(f"""INSERT INTO students 
                    (full_name, phone_number, age, is_have, direction, birth_date)
                    VALUES ('{full_name}', '{phone_number}', {age}, {is_have}, '{direction}', '{birth_date}')""")
            print("Вы успешно прошли регистрацию!")

        connect.commit()


    def all_students(self):
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print(students)

    def plus_student_rating(self):
        id = int(input("Введите id студента: "))
        new_rating = int(input("Введите кол-во рейтинга: "))

        cursor.execute(f"UPDATE students SET rating = rating + {new_rating} WHERE id = {id}")
        self.rating += new_rating
        self.rating = self.rating + new_rating
        connect.commit()

    def minus_student_rating(self):
        id = int(input("Введите id студента: "))
        new_rating = int(input("Введите кол-во рейтинга: "))

        cursor.execute(f"UPDATE students SET rating = rating - {new_rating} WHERE id = {id}")
        self.rating -= new_rating
        self.rating = self.rating - new_rating
        connect.commit()

    def delete_student(self):
        id = int(input("Введите id студента: "))
        cursor.execute(f"DELETE FROM students WHERE id = {id}")
        connect.commit()

    def main(self):
        while True:
            print("Выберите действие: ")
            print("""0-Выйти, 1-Регистрация, 2-Инфо всех студентов
3-Добавление балла к рейтингу, 4-Вычитание балла с рейтинга,
5-Удаление студента""")
            
            choice = int(input("Выберите цифру: "))
            if choice == 0:
                break
            elif choice == 1:
                self.register()
            elif choice == 2:
                self.all_students()
            elif choice == 3:
                self.plus_student_rating()
            elif choice == 4:
                self.minus_student_rating()
            elif choice == 5:
                self.delete_student()
            
            


students = GeeksStudents()
students.main()
