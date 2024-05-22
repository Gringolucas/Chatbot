import csv

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def registrarse(self):
        # Verificar si el email ya está registrado
        if self.email_existe(self.email):
            print("\nEl email ya está registrado. Por favor, ingrese otro email.\n")
            return False  # Indica que el registro no fue exitoso
        else:
            # Crear el archivo usuarios.csv si no existe
            self.crear_archivo_usuarios()

            # Guardar los datos del usuario en el archivo CSV
            with open('usuarios.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.nombre, self.email])
            print(f"\nBienvenido(a) {self.nombre}. Registro exitoso!\n")
            return True  # Indica que el registro fue exitoso

    def crear_archivo_usuarios(self):
        try:
            # Intentar abrir el archivo usuarios.csv en modo lectura
            with open('usuarios.csv', 'r') as file:
                pass  # No hacer nada si el archivo existe
        except FileNotFoundError:
            # Si el archivo no existe, crearlo con los encabezados de columna
            with open('usuarios.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Nombre', 'Email'])

    def obtener_informacion(self):
        return f"\nNombre: {self.nombre}, Email: {self.email}\n"

    def mostrar_historial(self):
        try:
            with open(f'{self.nombre}_historial.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row[0])
        except FileNotFoundError:
            print("No hay historial de conversación disponible.")

    @staticmethod
    def iniciar_sesion(nombre, email):
        # Verificar si el usuario está registrado en el archivo CSV
        with open('usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nombre and row[1] == email:
                    return True
        return False

    @staticmethod
    def email_existe(email):
        # Verificar si el email está registrado en el archivo CSV
        try:
            with open('usuarios.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == email:
                        return True
        except FileNotFoundError:
            return False
        return False