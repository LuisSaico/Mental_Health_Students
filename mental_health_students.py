"""En el proyecto Analizar la salud mental de los estudiantes en SQL, utilizarás tus conocimientos de PostgreSQL para
analizar los datos de los estudiantes de una universidad internacional japonesa y descubrir uno de los factores que más
influyen en la salud mental de los estudiantes internacionales.

La encuesta realizada por la universidad demostró que los principales retos para los estudiantes internacionales son la
conexión social y el estrés asociado a la incorporación a una nueva cultura. Tu tarea particular para este proyecto SQL
de principiante consistirá en centrarte en un factor contribuyente específico: la duración de la estancia y cómo influye
en las puntuaciones medias de diagnóstico de los estudiantes internacionales."""

import mysql.connector
import config

# CONNECTING WITH DATA BASE
connection = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database

)

cursor = connection.cursor()
# Creating database
# cursor.execute("CREATE DATABASE students")
# Creating table
table = """CREATE TABLE studentss ( id int not null auto_increment, Name Varchar(255) not null, Age int not null, 
Gender Varchar(255) not null, Student_id Varchar(255) not null, Mental_problem Varchar(255) not null, primary key(id))"""
# cursor.execute(table)

# List
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

# FUNCTION FOR INSERTING DATES


def inserting_dates(student):

    table = """INSERT INTO studentss (Name, Age, Gender, Student_id, Mental_problem) VALUES (%s, %s, %s, %s, %s)"""
    values = (student.name, student.age, student.gender, student.student_id, student.mental_problem)
    cursor.execute(table, values)
    connection.commit()

# FUNCTION FOR SHOW ALL THE STUDENTS


def show_students():

    cursor.execute("""SELECT * FROM studentss""")
    for (id, name, age, gender, student_id, mental_problem) in cursor.fetchall():

        print(f"#{id}\n"
              f"ID: {student_id}\n"
              f"Name: {name}\n"
              f"Age: {age}\n"
              f"Gender: {gender}\n"
              f"Mental Problem: {mental_problem}\n"
              f"------------------------------")

# FUNCTION FOR ANALYZE THE MOST COMMON PROBLEM IN THE STUDENTS


def analizating_dates():

    table = """SELECT CASE WHEN Mental_problem LIKE '%stress%' THEN 'stress'
    WHEN Mental_problem LIKE '%social%' THEN 'social'
    WHEN Mental_problem LIKE '%pressure%' THEN 'pressure'
    ELSE 'other'
    END AS student_problem, COUNT(*) AS amount FROM studentss GROUP BY student_problem
    ORDER BY amount DESC LIMIT 1;"""

    cursor.execute(table)
    dates = cursor.fetchone()

    if dates:
        student_problem, amount = dates
        print(f"The most common mental problem in the students is '{student_problem.upper()}' with {amount} students.")


# FUNCTION FOR DELETE STUDENTS


def delete_student(number_id):

    table = """DELETE FROM studentss WHERE id = %s"""
    cursor.execute(table, (number_id,))
    connection.commit()


# FUNCTION FOR UPDATE INFORMATION


def update_information(number_id, field, new_information):

    allowed_field = ["Name", "Age", "Gender", "Student_id", "Mental_problem"]
    if field not in allowed_field:
        raise ValueError(f"Error in {field}")

    table = f"""UPDATE studentss set {field} = %s WHERE id = %s"""
    values = (new_information, number_id)
    cursor.execute(table, values)
    connection.commit()


# MENU OF THE SYSTEM
def menu():

    print("||SAVING MIND||\n")

    while True:

        print("[1]-Register student\n"
              "[2]-Show the students\n"
              "[3]-Analyze dates\n"
              "[4]-Delete student\n"
              "[5]-Update information about the student\n"
              "[6]-Leave the system\n")

        choice = int(input("Enter your choice: "))
        print("=" * 30)

        # Registering students
        if choice == 1:
            name = input("Name of the student: ").lower()
            age = int(input("Age of the student: "))
            gender = input("Gender of the student: ").lower()
            student_id = input("Id of the student: ").lower()
            mental_problem = input("Mental problem of the student: ").lower()
            student = Student(name, age, gender, student_id, mental_problem)
            inserting_dates(student)
            print("Registered student")
            print("=" * 30)

        # Showing all the students
        elif choice == 2:
            show_students()

        # Showing dates
        elif choice == 3:
            analizating_dates()
            print("=" * 30)

        # Deleting student
        elif choice == 4:
            id_number = int(input("Enter id number that you want to delete: "))
            delete_student(id_number)
            print("Student deleted")
            print("=" * 30)

        # Updating information
        elif choice == 5:
            id_number = int(input("Enter id number that you want to delete: "))
            print(" ")
            print("-----------ALLOWED INFORMATION----------\n"
                  "|NAME|\n"
                  "|AGE|\n"
                  "|GENDER|\n"
                  "|ID|\n"
                  "|MENTAL PROBLEM|")
            print("-"*30)
            information = input("Enter what type of information about the student do you want to update: ").lower()
            new_information = input("Enter the new information about the student: ").lower()

            # Maping information about columns
            if information in ["name", "gender", "student id", "mental problem"]:
                new_information = str(new_information)

                if information == "student id":
                    information = "Student_id"

                elif information == "mental problem":
                    information = "Mental_problem"

                else:
                    information = information.capitalize()

            elif information == "age":
                new_information = int(new_information)
                information = "Age"

            else:
                print("INVALID OPTION")
                print("=" * 30)
                continue

            update_information(id_number, information, new_information)
            print("Updating information")
            print("=" * 30)

        # Leaving the system
        elif choice == 6:
            print("Leaving the system...")
            print("Thanks.")
            break

        # Invalid options
        else:
            print("Invalid choise. Please try it again")
            print("=" * 30)


# ----------MAIN----------
menu()
cursor.close()
connection.close()







