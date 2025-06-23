import numpy as np
from usuario import Usuario
from pelicula import Pelicula
from programacion import Programacion
from sala import Sala
from reserva import Reserva

class AppComplejo:
    """
    Esta es la clase principal del sistema, representa la aplicación general del complejo de cines.
    Es la encargada de inicializar los datos, manejar el flujo del sistema, y coordinar el acceso a 
    funcionalidades según el tipo de usuario autenticado.

    ATRIBUTOS:
    nombre: cadena de texto que representa el nombre del complejo de cines.
    direccion: cadena de texto que representa la dirección del complejo.
    usuario_autenticado: referencia al objeto Usuario autenticado actualmente.
    salas: arreglo de tamaño fijo que almacena objetos de la clase Sala.
    usuarios: arreglo que almacena la información de los usuarios del sistema.
    peliculas: arreglo que almacena las películas registradas en el sistema.
    reservas: arreglo que almacena las reservas realizadas por los clientes.
    cont_salas: contador que indica cuántas salas han sido registradas.
    cont_usuarios: contador que indica cuántos usuarios han sido registrados.
    cont_peliculas: contador que indica cuántas películas han sido registradas.
    cont_reservas: contador que indica cuántas reservas se han realizado.

    CONSTANTES:
    MAX_SALAS: número máximo de salas que puede tener el complejo (12).
    """

    #atributos
    #*nombre = str
    #*direccion = str
    #*usuario_autenticado = Usuario
    #*salas = np.ndarray
    #*usuarios = np.ndarray
    #*peliculas = np.ndarray
    #*reservas = np.ndarray
    #*cont_salas = int
    #*cont_usuarios = int
    #*cont_peliculas = int
    #*cont_reservas = int
    
    #constantes
    MAX_SALAS = 12
    
    # Constructor de la clase
    def __init__(self):
        #datos generales del complejo
        self.nombre = "¿Qué hay para ver?"
        self.direccion = "Calle 123 N°345"
        self.usuario_autenticado = None
        
        #Arreglo fijos de salas, usuarios, películas y reservas 
        self.salas = np.empty(self.MAX_SALAS, dtype=object)
        self.usuarios = np.empty(100, dtype=object)
        self.peliculas = np.empty(100, dtype=object)
        self.reservas = np.empty(200, dtype=object)

        #Contadores para los arreglos
        self.cont_salas = 0
        self.cont_usuarios = 0
        self.cont_peliculas = 0
        self.cont_reservas = 0
        
        
    def ejecutar(self):
        """
        Método que ejecuta el inicio de la aplicación
        """
        opc = 0
        
        while opc != 3:
            print("MENÚ".center(40,"="))
            print("1. Iniciar sesion\n2. Registrarse\n3. Salir de la app")
            
            try:
                opc = int(input("Ingrese su elección: "))
            except ValueError:
                print("ERROR: entrada invalida")
                opc = 0
            
            match opc:
                case 1:
                    if self.autenticar_usuario():
                        if self.usuario_autenticado.tipo == Usuario.TIPO_ADMIN:
                            self.mostrar_menu_admin()
                        elif self.usuario_autenticado.tipo == Usuario.TIPO_VENDEDOR:
                            self.mostrar_menu_vendedor()
                        elif self.usuario_autenticado.tipo == Usuario.TIPO_CLIENTE:
                            self.mostrar_menu_cliente()
                        else:
                            print("Tipo de usuario no reconocido")
                case 2:
                    self.registrar_usuario()
                case 3:
                    print("APLICACIÓN TERMINADA")
                case _:
                    print("Opción invalida")
    
    def mostrar_menu_admin(self):
        """
        Este método muestra el menú de opciones para un administrador.
        """
        print(f"\nBienvenido, {self.usuario_autenticado.nombre}")
        while True:
            print("\nMENÚ ADMINISTRADOR".center(40, "="))
            print("1. Registrar usuario")
            print("2. Registrar pelicula")
            print("3. Modificar estado de película")
            print("4. Cambiar tipo de usuario")
            print("5. Registrar Sala")
            print("6. Consultar programación por sala")
            print("7. Consultar funciones de una película")
            print("8. Ver detalle de una película")
            print("9. Cerrar sesión")

            try:
                opc = int(input("Seleccione una opción: "))
            except ValueError:
                print("ERROR: entrada inválida")
                continue

            match opc:
                case 1:
                    self.registrar_usuario()
                case 2:
                    self.registrar_pelicula()
                case 3:
                    self.modificar_estado_pelicula()
                case 4:
                    self.modificar_tipo_usuario()
                case 5:
                    self.registrar_sala()
                case 6:
                    self.consultar_programacion_sala()
                case 7:
                    self.consultar_funciones_pelicula()
                case 8:
                    self.ver_detalle_pelicula()
                case 9:
                    self.usuario_autenticado = None
                    break
                case _:
                    print("Opción no válida")


    def mostrar_menu_vendedor(self):
        """
        Este método muestra el menu de opciones de un vendedor.
        """
        print(f"\nBienvenido, {self.usuario_autenticado.nombre}")
        while True:
            print("\nMENÚ VENDEDOR".center(40, "="))
            print("1. Registrar usuario")
            print("2. Consultar programación por sala")
            print("3. Consultar funciones de una película")
            print("4. Ver detalle de una película")
            print("5. Cerrar sesión")

            try:
                opc = int(input("Seleccione una opción: "))
            except ValueError:
                print("ERROR: entrada inválida")
                continue

            match opc:
                case 1:
                    self.registrar_usuario()
                case 2:
                    self.consultar_programacion_sala()
                case 3:
                    self.consultar_funciones_pelicula()
                case 4:
                    self.ver_detalle_pelicula()
                case 5:
                    self.usuario_autenticado = None
                    break
                case _:
                    print("Opción no válida")
    
    def mostrar_menu_cliente(self):
        """
        Este método muestra el menu de opciones de un cliente.
        """
        print(f"\nBienvenido, {self.usuario_autenticado.nombre}")
        while True:
            print("\nMENÚ CLIENTE".center(30, "="))
            print("1. Ver detalle de una película")
            print("2. Consultar funciones de una película")
            print("3. Cerrar sesión")

            try:
                opc = int(input("Seleccione una opción: "))
            except ValueError:
                print("ERROR: entrada inválida")
                continue

            match opc:
                case 1:
                    self.ver_detalle_pelicula()
                case 2:
                    self.consultar_funciones_pelicula()
                case 3:
                    self.usuario_autenticado = None
                    break
                case _:
                    print("Opción no válida")

    def autenticar_usuario(self):
        """
        Este método permite autenticar a un usuario
        Returns:
            bool: Retorna True si se pudo autenticar el usuario, False en caso contrario
        """
        # Se piden los datos de autenticación
        print ("AUTENTICACIÓN DE USUARIO".center(40,"="))
        ced = input("Ingrese el número de documento del usuario: ").strip()
        pas = input("Ingrese la contraseña del usuario: ").strip()
        
        # Se recorre el arreglo de usuarios en busqueda del usuario a autenticar
        for i in range(self.cont_usuarios):
            # si se encuentra el usuario procede a comprobar la contraseña
            if self.usuarios[i].cedula == ced:
                # si la contraseña es valida se actualiza el usuario autenticado y se retorna True
                if self.usuarios[i].contrasena == pas:
                    self.usuario_autenticado = self.usuarios[i]
                    return True
                # si la contraseña no es valida se muestra un mensaje y se retorna False
                else:
                    input("La contraseña ingresada no coincide con la contraseña del usuario. Presione enter para continuar ...")
                    return False
        
        # Si no se encuentra el usuario se muestra un mensaje y se retorna False
        input(f"El usuario con cedula {ced} no está registrado. Presione enter para continuar ...")
        return False

    def registrar_usuario(self):
        """
        Este método permite registrar un nuevo usuario en el sistema.
        """
        print ("REGISTRO DE USUARIOS".center(40,"="))
        # si aun hay espacio para registra un nuevo usuario se inicializa uno nuevo y se piden sus datos
        if self.cont_usuarios < len(self.usuarios):
            usr = Usuario()
            usr.pedir_datos()

            # se recorre el arreglo de usuarios para comprobar si el usuario ya se encuentra registrado
            existe = False
            for i in range(self.cont_usuarios):
                if self.usuarios[i].cedula == usr.cedula:
                    existe = True
                    break
            
            # si no está registrado se agrega al arreglo de usuario, se actualiza el contador y se muestra un mensaje de exito
            if not existe:
                self.usuarios[self.cont_usuarios] = usr
                self.cont_usuarios += 1
                print("Usuario registrado con éxito")
            # en caso contrario se indica que ya esta registrado
            else:
                input("Ya hay un usuario registrado con esa cedula. Presione enter para continuar ...")
        else:
            input("No es posible registrar más usuarios. Presione enter para continuar ...")
    
    def modificar_tipo_usuario(self):
        """
        Este método permite al administrador cambiar el tipo de un usuario ya registrado,
        solicitando la cédula y el nuevo tipo.
        """
        ced = input("Ingrese el número de documento del usuario: ").strip()
        try:
            nuevo_tipo = int(input("Ingrese el nuevo tipo de usuario (1: Cliente, 2: Vendedor, 3: Administrador): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return

        # se recorre el arreglo de usuarios buscando el que coincida con la cedula ingresada
        for i in range(self.cont_usuarios):
            # si se encuentra la cedula se realiza el cambio de tipo desde el usuario
            if self.usuarios[i].cedula == ced:
                if self.usuarios[i].cambiar_tipo(nuevo_tipo):
                    print("Tipo de usuario actualizado.")
                return

        input("No se encontró ningún usuario con esa cédula. Presione enter para continuar ...")

    def registrar_pelicula(self):
        """
        Este método permite registrar un nueva película en el sistema.
        """
        print ("REGISTRO DE PELICULAS".center(40,"="))
        # si aun hay espacio para registra una pelicula se crea y se piden sus datos
        if self.cont_peliculas < len(self.peliculas):
            peli = Pelicula()
            peli.pedir_datos()
            
            existe = False
            for i in range(self.cont_peliculas):
                if self.peliculas[i].nombreEsp == peli.nombreEsp:
                    existe = True
                    break
            
            if not existe:
                self.peliculas[self.cont_peliculas] = peli
                self.cont_peliculas += 1
                print("Se registro la pelicula con exito")
            else:
                input("Ya hay una película registrada con este nombre. Presione enter para continuar ...")
        else:
            input("No es posible registrar más películas. Presione enter para continuar ...")
    
    def modificar_estado_pelicula(self):
        """
        Este método permite al administrador cambiar el estado de una pelicula.
        """
        nomPeli = input("Ingrese el nombre de la película en español: ").strip().title()
        try:
            nuevo_estado = int(input("Ingrese el nuevo estado de la película (1: Activo, 0: Inactivo): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return

        for i in range(self.cont_peliculas):
            if self.peliculas[i].nombreEsp == nomPeli:
                if self.peliculas[i].cambiar_estado(nuevo_estado):
                    print("Estado actualizado.")
                return
        
        input("No se encontró ningúna película con ese nombre. Presione enter para continuar ...")
    
    def ver_detalle_pelicula(self):
        """
        Este método permite al usuario consultar el detalle completo de una película registrada.
        """
        print(f"Películas registradas: {[self.peliculas[i].nombreEsp for i in range(self.cont_peliculas)]}")
        print("\nCONSULTAR DETALLE DE PELÍCULA".center(40, "="))
        nomPeli = input("Ingrese el nombre de la película en español: ").strip()

        for i in range(self.cont_peliculas):
            if self.peliculas[i].nombreEsp.lower() == nomPeli.lower():
                self.peliculas[i].mostrar_detalle()
                return
        
        input("No se encontró ningúna película con ese nombre. Presione enter para continuar ...")
    
    def consultar_programacion_general(self):
        """
        Este método permite consultar la programación completa del complejo, 
        mostrando las funciones programadas en cada sala.
        """
        print("\nPROGRAMACIÓN GENERAL DEL COMPLEJO".center(40, "="))

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        for i in range(self.cont_salas):
            self.salas[i].mostrar_programacion()
    
    def consultar_programacion_sala(self):
        """
        Este método permite consultar la programación de una sala en específico, 
        mostrando todas las funciones programadas en la sala.
        """
        print("\nCONSULTA PROGRAMACIÓN DE SALA".center(40, "="))
        try:
            idSala = int(input("Ingrese el ID de la sala que desea consultar: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        for i in range(self.cont_salas):
            if self.salas[i].id == idSala:
                self.salas[i].mostrar_programacion()
                return

        input(f"No se encontró ninguna sala con ID {idSala}. Presione enter para continuar ...")


    def consultar_funciones_pelicula(self):
        """
        Este método permite consultar las funciones programadas de una película específica,
        mostrando en qué salas y horarios se encuentra actualmente programada.
        """
        print("\nCONSULTA FUNCIONES DE UNA PELÍCULA".center(40, "="))
        peli = input("Ingrese el nombre de la película que desea buscar: ").strip().title()

        if self.cont_peliculas == 0:
            input("No hay películas registradas aún. Presione enter para continuar ...")
            return

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        encontrada = False

        for i in range(self.cont_salas):
            for j in range(self.salas[i].cont_programacion):
                prog = self.salas[i].programacion[j]
                if prog.pelicula.nombreEsp == peli:
                    print(f"Sala {self.salas[i].id} - Horario: {prog.horario}")
                    encontrada = True

        if not encontrada:
            input("La película no se encuentra programada actualmente. Presione enter para continuar ...")
    
    def registrar_sala(self):
        """
        Este método permite registrar una nueva sala en el sistema.
        """
        print("REGISTRO DE SALAS".center(40, "="))

        if self.cont_salas < len(self.salas):
            sala = Sala(id=self.cont_salas + 1)
            sala.pedir_datos()
            self.salas[self.cont_salas] = sala
            self.cont_salas += 1
            print("Sala registrada con éxito.")
        else:
            input("Ya no es posible crear más salas. Presione enter para continuar ...")

    def agregar_funcion(self):
        pass

    def eliminar_funcion(self):
        pass

    def modificar_horario_funcion(self):
        pass
    
    def eliminar_funciones_pelicula(self):
        pass

    def realizar_reserva(self):
        pass

    def consultar_ocupacion(self):
        pass

    def consultar_recaudo_sala(self):
        pass

    def consultar_recaudo_total(self):
        pass
    
    def cargar_datos_prueba(self):
        """
        Carga datos de prueba en el sistema para facilitar las pruebas interactivas:
        usuarios de todos los tipos, una sala básica y una película registrada.
        """

        # Usuarios
        self.usuarios[0] = Usuario(nombre="Camila Admin", cedula="1001", contrasena="admin123")
        self.usuarios[0].cambiar_tipo(Usuario.TIPO_ADMIN)

        self.usuarios[1] = Usuario(nombre="Pedro Vendedor", cedula="1002", contrasena="vend123")
        self.usuarios[1].cambiar_tipo(Usuario.TIPO_VENDEDOR)

        self.usuarios[2] = Usuario(nombre="Laura Cliente", cedula="1003", contrasena="cli123")
        # Tipo cliente por defecto

        self.cont_usuarios = 3

        # Película
        peli = Pelicula(
            nombreEsp="Titanes del Pacifico",
            nombreOriginal="Pacific Rim",
            anioEstreno=2013,
            duracion=131,
            genero="Acción",
            paisOrigen="EE.UU.",
            calificacion=4.2
        )
        self.peliculas[0] = peli
        self.cont_peliculas = 1

        # Sala
        sala = Sala(id=1, valorBoleta=15000, filas=5, asientosFila=6)
        self.salas[0] = sala
        self.cont_salas = 1

        print("Datos de prueba cargados correctamente.")



App = AppComplejo()
App.cargar_datos_prueba()
App.ejecutar()