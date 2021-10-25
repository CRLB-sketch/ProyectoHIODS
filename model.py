# Modelo
# Controllar los datos
import pandas as pd
import matplotlib.pyplot as plt

class Person:    
    def __init__(self, name, email):
        self.name = name        
        self.email = email        

class Student(Person):
    def __init__(self, name, last_name, phone, email, type_help):
        Person.__init__(self, name, email)
        self.last_name = last_name
        self.phone = phone
        self.type_help = type_help        

class Voluntary(Person):
    def __init__(self, name, type_help, email, phone, courses):
        Person.__init__(self, name, email)
        self.courses = courses
        self.phone = phone
        self.type_help = type_help

class Donation(Person):
    def __init__(self, name, email, donated_money, others_donated):
        Person.__init__(self, name, email)
        self.donated_money = donated_money
        self.others_donated = others_donated
        
class Model:
    FILE_STUDENTS = "docs//students.csv"
    FILE_VOLUNNTEERING = "docs//volunteering.csv"
    FILE_INSTITUTIONS = "docs//institutions.csv"
    FILE_DONATIONS = "docs//donations.csv"
    FILE_INFORMATION = "docs//information.csv"

    def __init__(self):
        self.df_students = pd.read_csv(self.FILE_STUDENTS, encoding="latin1")
        self.df_volunnteering = pd.read_csv(self.FILE_VOLUNNTEERING, encoding="latin1")
        self.df_donations = pd.read_csv(self.FILE_DONATIONS, encoding="latin1")
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

    def add_new_donnation(self, donation : Donation):
        new_registry = {
            "name" : donation.name,
            "email" : donation.email,
            "donated_money" : donation.donated_money,
            "others_donated" : donation.others_donated,
        }

        self.df_donations = self.df_donations.append(new_registry, ignore_index=True)
        self.df_donations.to_csv(self.FILE_DONATIONS, index=False)
        return "Información guardada con éxito"

    def add_count_visite(self):
        self.df_information["veces_estudiante_interaccion"][0] += 1
        self.df_information.to_csv(self.FILE_INFORMATION, index=False)

    # --> Métodos para llevar mostrar información en específica
    def show_recomendation_complete(self, type_help):
        total_elements = self.df_institutions.shape[0]
        for i in range(total_elements):
            if self.df_institutions["tipobeca"][i] == type_help or self.df_institutions["tipobeca"][i] == "Mixto":
                print(f"-> {self.df_institutions['nombre'][i]} - Descripcion:\n{self.df_institutions['detalles'][i]}\n")

    def show_other_recomendations(self):
        total_elements = self.df_institutions.shape[0]
        for i in range(total_elements):
            if self.df_institutions["tipobeca"][i] != "Completa" or self.df_institutions["tipobeca"][i] != "Parcial":
                print(f"-> {self.df_institutions['nombre'][i]} - Descripcion:\n{self.df_institutions['detalles'][i]}\n")

    # --> Métodos para llevar a cabo el análisis de datos
    def get_information_general(self):
        info = f"""
        Estudiantes que ingresaron a la pagina: {self.df_information["veces_estudiante_interaccion"][0]}
        Cantidad de estudiantes registrados: {self.df_students.shape[0]}        
        """
        return info

    def get_donations_recived(self):
        info = f""     
        
        money = 0
        elements = self.df_donations.shape[0]
        # Mostrar dinero donado
        for i in range(elements): money += int(self.df_donations["donated_money"][i])
        info += f"\nDinero donado en total: {money}\n"

        # Mostrar elementos donados
        info += f"\nElementos donados:\n"
        for i in range(elements): 
            donated_elems = self.df_donations["others_donated"][i].split("+")
            for elem in donated_elems: 
                if not len(elem) == 0:
                    info += f"-> {elem}\n"

        return info

    def show_grafic(self, type):
        prueba = {"Cantidad que entraron a la página" : self.df_information["veces_estudiante_interaccion"][0],
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
