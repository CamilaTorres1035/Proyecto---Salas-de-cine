
class Usuario:
    """
    Clase que representa a un usuario del sistema. Puede ser cliente, vendedor o administrador.

    ATRIBUTOS:
    nombre: cadena que representa el nombre completo del usuario.
    cedula: cadena que representa el número de documento del usuario.
    correo: cadena que representa el correo electrónico del usuario.
    telefono: cadena que representa el número de teléfono del usuario.
    contrasena: cadena que almacena la contraseña de acceso del usuario.
    tipo: entero que representa el tipo de usuario (1: cliente, 2: vendedor, 3: administrador).

    CONSTANTES:
    TIPO_CLIENTE: constante con valor 1 que representa un cliente.
    TIPO_VENDEDOR: constante con valor 2 que representa un vendedor.
    TIPO_ADMIN: constante con valor 3 que representa un administrador.
    
    Autor: Camila Torres
    Fecha de creación: 30/05/2024
    """
    nombre = str
    cedula = str
    correo = str
    telefono = str
    contrasena = str
    tipo = int
    
    TIPO_CLIENTE = 1
    TIPO_VENDEDOR = 2
    TIPO_ADMIN = 3
    
    # Constructor de la clase
    def __init__(self, nombre="", cedula="", correo="", telefono="", contrasena=""):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.contrasena = contrasena
        self.tipo = self.TIPO_CLIENTE

    def pedir_datos(self):
        """
        Este método pide por consola los datos básicos del usuario.
        """
        while True:
            self.nombre = input("Ingrese el nombre completo del usuario: ").strip()
            if self.nombre: break
            print("El nombre no puede estar vacío.")

        while True:
            self.cedula = input("Ingrese el número de documento: ").strip()
            if self.cedula.isdigit(): break
            print("La cédula debe ser numérica.")

        while True:
            self.correo = input("Ingrese el correo: ").strip()
            if "@" in self.correo and "." in self.correo: break
            print("El correo no es válido.")

        while True:
            self.telefono = input("Ingrese el número de teléfono: ").strip()
            if self.telefono.isdigit() and len(self.telefono) >= 7: break
            print("El número de teléfono debe ser numérico y tener al menos 7 dígitos.")

        while True:
            self.contrasena = input("Ingrese la contraseña: ").strip()
            if len(self.contrasena) >= 4: break
            print("La contraseña debe tener al menos 4 caracteres.")
    
    def cambiar_tipo(self, nuevo_tipo):
        """
        Este metodo sirve para cambiar el tipo de usuario a un usuario.

        Parametros:
        nuevo_tipo: Nuevo tipo de usuario.
        """
        if nuevo_tipo in (self.TIPO_ADMIN, self.TIPO_VENDEDOR, self.TIPO_CLIENTE):
            self.tipo = nuevo_tipo
            return True
        print("El tipo de usuario ingresado es invalido")
        return False
