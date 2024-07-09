"""En el proyecto Analizar la salud mental de los estudiantes en SQL, utilizarás tus conocimientos de PostgreSQL para
analizar los datos de los estudiantes de una universidad internacional japonesa y descubrir uno de los factores que más
influyen en la salud mental de los estudiantes internacionales.

La encuesta realizada por la universidad demostró que los principales retos para los estudiantes internacionales son la
conexión social y el estrés asociado a la incorporación a una nueva cultura. Tu tarea particular para este proyecto SQL
de principiante consistirá en centrarte en un factor contribuyente específico: la duración de la estancia y cómo influye
en las puntuaciones medias de diagnóstico de los estudiantes internacionales."""

import mysql.connector

# Lists
invalid_dates = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# CREATING FATHER CLASS


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# CREATING SON CLASS
class Student(Person):

    def __init__(self, name, age, gender, student_id, mental_problem):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.mental_problem = mental_problem

    # Show Dates of the student
    def __str__(self):
        return (f"Name of the student: {self.name}\n"
                f"Age of the student: {self.age}\n"
                f"Gender of the student: {self.gender}\n"
                f"Id of the student: {self.student_id}\n"
                f"Mental problem of the student: {self.mental_problem}")

    # Ask for the mental health problem
    @staticmethod
    def ask(limit_students):

        students = []

        for _ in range(limit_students):

            name = input("Enter the name of the student: ")
            age = int(input("Enter the age of the student: "))
            gender = input("Enter the gender of the estudent: ")
            idd = input("Enter the id of the student: ")
            problem = input("Enter the mental problem of the student: ")
            student = Student(name, age, gender, idd, problem)
            students.append(student)


# MENU OF THE SYSTEM
def menu(student):

    print("||SAVING MIND||\n")

    while True:

        print("[1]-Register student\n"
              "[2]-Show the students\n"
              "[3]-Leave the system\n")

        choice = int(input("Enter your choice: "))
        print("=" * 30)

        if choice == 1:
            student.ask()

        elif choice == 2:
            print("showing")

        elif choice == 3:
            print("Leaving the system...")
            print("Thanks.")












