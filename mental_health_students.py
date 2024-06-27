"""En el proyecto Analizar la salud mental de los estudiantes en SQL, utilizarás tus conocimientos de PostgreSQL para
analizar los datos de los estudiantes de una universidad internacional japonesa y descubrir uno de los factores que más
influyen en la salud mental de los estudiantes internacionales.

La encuesta realizada por la universidad demostró que los principales retos para los estudiantes internacionales son la
conexión social y el estrés asociado a la incorporación a una nueva cultura. Tu tarea particular para este proyecto SQL
de principiante consistirá en centrarte en un factor contribuyente específico: la duración de la estancia y cómo influye
en las puntuaciones medias de diagnóstico de los estudiantes internacionales."""

# Lists
mental_healt_problem = []
invalid_dates = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# CREATING FATHER CLASS


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# CREATING SON CLASS
class Student(Person):

    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    # Show Dates of the student
    def __str__(self):
        return (f"Name of the student: {self.name}\n"
                f"Age of the student: {self.age}\n"
                f"Gender of the student: {self.gender}\n"
                f"Id of the student: {self.student_id}")

    # Ask for the mental health problem
    @staticmethod
    def ask():

        problem = input("Enter the mental problem of the student: ")

        # Evaluating invalid date
        for number in invalid_dates:
            if number in problem:
                while True:
                    problem = input("Enter the mental problem of the student: ")
                    if number in problem:
                        continue
                    else:
                        mental_healt_problem.append(problem)
                        break











