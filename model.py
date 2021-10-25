# Modelo
# Controllar los datos
import pandas as pd
import matplotlib.pyplot as plt

class Person:
    def __init__(self, name, phone, email, type_help):
        self.name = name
        self.phone = phone
        self.email = email
        self.type_help = type_help

class Student(Person):
    def __init__(self, name, last_name, phone, email, type_help):
        Person.__init__(self, name, phone, email, type_help)
        self.last_name = last_name

class Voluntary(Person):
    def __init__(self, name, type_help, email, phone, courses):
        Person.__init__(self, name, phone, email, type_help)
        self.courses = courses

class Model:

    FILE_STUDENTS = "docs//students.csv"
    FILE_VOLUNNTEERING = "docs//volunteering.csv"
    FILE_INSTITUTIONS = "docs//institutions.csv"
    FILE_INFORMATION = "docs//information.csv"

    def __init__(self):
        self.df_students = pd.read_csv(self.FILE_STUDENTS, encoding="latin1")
        self.df_volunnteering = pd.read_csv(self.FILE_VOLUNNTEERING, encoding="latin1")
        self.df_institutions = pd.read_csv(self.FILE_INSTITUTIONS, encoding="latin1")
        self.df_information = pd.read_csv(self.FILE_INFORMATION, encoding="latin1")
    
    # --> Métodos para agregar datos nuevos a las "bases de datos"
    def add_new_student(self, student : Student):
        new_registry = {
            "nombre" : student.name,
            "apellido" : student.last_name,
            "correo" : student.email,
            "numero" : student.phone,
            "tipo_ayuda_buscada" : student.type_help
        }

        self.df_students = self.df_students.append(new_registry, ignore_index=True)
        self.df_students.to_csv(self.FILE_STUDENTS, index=False)
        return "Información guardada con éxito"

    def add_new_voluntary(self, voluntary : Voluntary):
        new_registry = {
            "nombre_voluntariado" : voluntary.name,
            "tipo_ayuda" : voluntary.phone,
            "correo" : voluntary.email,
            "numero_telefonico" : voluntary.phone,
            "cuantcursos" : voluntary.courses
        }

        self.df_volunnteering = self.df_volunnteering.append(new_registry, ignore_index=True)
        self.df_volunnteering.to_csv(self.FILE_VOLUNNTEERING, index=False)
        return "Información guardada con éxito"

    # --> Métodos para llevar a cabo el análisis de datos
    def get_information_general(self):
        info = f"""
        Estudiantes que ingresaron a la pagina: {self.df_information["veces"][0]}
        Cantidad de estudiantes registrados: {self.df_students.shape[0]}
        Dinero recolectado: {self.df_information["dinero"][0]}
        """
        return info

    def get_donations_recived(self):
        info = ""     

        info += "\nComputadoras: \n" + self.df_information["computadoras"][0] + "\n"
        info += "\nCuadernos: \n" + self.df_information["cuadernos"][0] + "\n"
        info += "\nOtros: \n" + self.df_information["otros"][0] + "\n"

        return info

    def show_grafic(self, type):
        prueba = {"Cantidad que entraron a la página" : self.df_information["veces"][0],
            "Estudiantes registrados" : self.df_students.shape[0]} if type == 1 else {"Estudiantes" : self.df_students.shape[0],
            "Voluntareados" : self.df_volunnteering.shape[0],
            "Instituciones" : self.df_institutions.shape[0]}

        dates = list(prueba.keys())
        values = list(prueba.values())

        plt.bar(dates, values, color = "red", width = 0.4)

        plt.title("Estudiantes ingresados")
        plt.ylabel("Cantidad Control")
        plt.xlabel("Tipo de interacción")
        plt.show()        
