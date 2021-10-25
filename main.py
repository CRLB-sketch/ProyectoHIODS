from model import Model, Student, Voluntary # Para programa sin interfaz (solo en consola)

def main():
    finish = False
    while not finish:
        # Solo llamaré al modelo para obtener toda la lógica del caso
        model = Model()

        # Esto lo tomaré como si fuera mi vista y controlador por el momento jsjs
        print("Menu")
        print("1. ¿Necesitas apoyo?")
        print("2. ¿Quisieras ser voluntario?")
        print("3. ¿Te gustaría apoyar?")
        print("4. Ver estadísticas y datos")
        print("5. Terminar")
        option = input()

        # Necesitas apoyo <-------------------------------------------
        if option == "1":

            # Solicitar alguna información importante
            name = _check_field("nombre")
            last_name = _check_field("apellido")
            phone = _check_field("telefono")
            email = _check_field("correo")

            # Preguntar que tipo de ayuda necesita
            type_help = ""
            valid = False
            while not valid:
                print("¿Buscas apoyo financiero?")
                print("1. Beca completa")
                print("2. Apoyo parcial")
                print("3. Yo puedo pagar la univerdad por mi cuenta")

                option = input()

                if option == '1':
                    valid = True
                    type_help = "beca_completa"
                elif option == '2':
                    valid = True
                    type_help = "beca_parcial"
                elif option == '3':
                    valid = True
                    type_help = "no_necesita_ayuda"
                else:
                    print("Porfavor ingresa una opción válida")
                
            # Agregar al nuevo estudiante
            new_student = Student(name, last_name, phone, email, type_help)
            print(model.add_new_student(new_student))
                        
        # ¿Quisieras ser voluntario? <-------------------------------------------
        elif option == "2":

            type_help = ""
            valid = False
            while not valid:
                print("¿Que tipo de voluntariado deseas hacer?")
                print("1. Tutor")
                print("2. Acompañiante")

                option = input()

                if option == "1" or option == "2":
                    valid = True
                    type_help = "tutor" if option == "1" else "acompaniante"
                else:
                    print("Porfavor ingrese una opción válida")


            name = _check_field("nombre")
            phone = _check_field("telefono")
            email = _check_field("email")

            courses = ""
            valid = False
            count = 0
            while not valid:
                print("Ingrese nombre de curso que desea dar")
                mesagge = "Por el momento no deseo/puedo apoyar por medio de un curso (presiona 'Q') para salir.\n" if count == 0 else "Con esto basta (presiona 'Q')\n"
                name_course = input(mesagge).upper()

                if len(name_course) == 0:
                    print("Porfavor ingresa una opción o un curso")
                elif "+" in name_course:
                    print("Porfavor no ingrese este signo para el nombre del curso")
                elif "," in name_course:
                    print("Porfavor no ingrese comas en este tipo de campo")
                elif name_course == "Q":
                    valid = True
                else:
                    courses += name_course + "+"
                    count += 1

            new_voluntary = Voluntary(name, type_help, email, phone, courses)
            print(model.add_new_voluntary(new_voluntary))

        # ¿Te gustaría apoyar? <-------------------------------------------------
        elif option == "3":
            print("")

        # Estadísticas y datos <-------------------------------------------------
        elif option == "4":
            _see_statics(model)

        # Terminar con el programa <---------------------------------------------
        elif option == "5":
            finish = True
            print("Terminando....")

        else:
            print("-> Opción inválida")
    
def _check_field(type_requested):
    field = ""
    while len(field) == 0:
        field = input(f"Porfavor ingrese su {type_requested}: ")

        if len(field) == 0:
            print(f"\nPorfavor no deje vacio el campo para ingresar el {type_requested}\n")
        elif "," in field:
            print("Porfavor no ingrese comas en este tipo de campo")
            field = ""

    return field

def _see_statics(model : Model):
    finish = False

    while not finish:
        print("¿Que deseas ver?")
        print("1. Información general")
        print("2. Donaciones Recibidas")
        print("3. Gráfica de interacción de estudiantes")
        print("4. Gráfica cantidad de involucrados")
        print("5. Regresar al menu principal")

        option = input()

        if option == "1": 
            print(model.get_information_general())

        elif option == "2": 
            print(model.get_donations_recived())

        elif option == "3": 
            model.show_grafic(1)

        elif option == "4": 
            model.show_grafic(0)

        elif option == "5": 
            finish = True

        else:
            print("-> Opción inválida")
        

from controller import Controller # Para programa con interfaz

if __name__ == '__main__':
    # df_estudiantes = pd.read_csv("docs//students.csv", encoding="latin1")
    # print(df_estudiantes)

    ############################################
    main()
    ############################################
    # system = Controller()
    # system.main()
