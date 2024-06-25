"""En el proyecto Analizar la salud mental de los estudiantes en SQL, utilizarás tus conocimientos de PostgreSQL para
analizar los datos de los estudiantes de una universidad internacional japonesa y descubrir uno de los factores que más
influyen en la salud mental de los estudiantes internacionales.

La encuesta realizada por la universidad demostró que los principales retos para los estudiantes internacionales son la
conexión social y el estrés asociado a la incorporación a una nueva cultura. Tu tarea particular para este proyecto SQL
de principiante consistirá en centrarte en un factor contribuyente específico: la duración de la estancia y cómo influye
en las puntuaciones medias de diagnóstico de los estudiantes internacionales."""

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
