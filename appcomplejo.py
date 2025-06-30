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
            print("2. Registrar película")
            print("3. Modificar estado de película")
            print("4. Cambiar tipo de usuario")
            print("5. Registrar sala")
            print("6. Programar función")
            print("7. Modificar horario de función")
            print("8. Eliminar función")
            print("9. Consultar programación por sala")
            print("10. Consultar funciones de una película")
            print("11. Ver detalle de una película")
            print("12. Realizar reserva")
            print("13. Consultar ocupación por función")
            print("14. Consultar recaudo por sala")
            print("15. Consultar recaudo total del complejo")
            print("16. Cerrar sesión")

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
                    self.agregar_funcion()
                case 7:
                    self.modificar_horario_funcion()
                case 8:
                    self.eliminar_funcion()
                case 9:
                    self.consultar_programacion_sala()
                case 10:
                    self.consultar_funciones_pelicula()
                case 11:
                    self.ver_detalle_pelicula()
                case 12:
                    self.realizar_reserva()
                case 13:
                    self.consultar_ocupacion()
                case 14:
                    self.consultar_recaudo_sala()
                case 15:
                    self.consultar_recaudo_total()
                case 16:
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
            print("5. Realizar reserva")
            print("6. Cerrar sesión")

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
                    self.realizar_reserva()
                case 6:
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
            print("\nMENÚ CLIENTE".center(40, "="))
            print("1. Ver detalle de una película")
            print("2. Consultar funciones de una película")
            print("3. Realizar reserva")
            print("4. Cerrar sesión")

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
                    self.realizar_reserva()
                case 4:
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
                input("Usuario registrado con éxito. Presione enter para continuar ...")
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
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        # se recorre el arreglo de usuarios buscando el que coincida con la cedula ingresada
        for i in range(self.cont_usuarios):
            # si se encuentra la cedula se realiza el cambio de tipo desde el usuario
            if self.usuarios[i].cedula == ced:
                if self.usuarios[i].cambiar_tipo(nuevo_tipo):
                    input("Tipo de usuario actualizado. Presione enter para continuar ...")
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
                input("Se registro la pelicula con exito. Presione enter para continuar ...")
            else:
                input("Ya hay una película registrada con este nombre. Presione enter para continuar ...")
        else:
            input("No es posible registrar más películas. Presione enter para continuar ...")
    
    def modificar_estado_pelicula(self):
        """
        Este método permite al administrador cambiar el estado de una película.
        Si se desactiva, también elimina todas sus funciones programadas en el complejo.
        """
        nomPeli = input("Ingrese el nombre de la película en español: ").strip()
        try:
            nuevo_estado = int(input("Ingrese el nuevo estado de la película (1: Activo, 0: Inactivo): "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        for i in range(self.cont_peliculas):
            if self.peliculas[i].nombreEsp.lower() == nomPeli.lower():
                if self.peliculas[i].cambiar_estado(nuevo_estado):
                    input("Estado actualizado. Presione enter para continuar ...")
                    if nuevo_estado == Pelicula.ESTADO_INACTIVO:
                        self.eliminar_funciones_pelicula(nomPeli)
                        input("Se eliminaron las funciones programadas de esta película. Presione enter para continuar ...")
                return
        
        input("No se encontró ningúna película con ese nombre. Presione enter para continuar ...")
    
    def ver_detalle_pelicula(self):
        """
        Este método permite al usuario consultar el detalle completo de una película registrada.
        """
        print("\nCONSULTAR DETALLE DE PELÍCULA".center(40, "="))
        nomPeli = input("Ingrese el nombre de la película en español: ").strip()

        for i in range(self.cont_peliculas):
            if self.peliculas[i].nombreEsp.lower() == nomPeli.lower():
                self.peliculas[i].mostrar_detalle()
                input("Presione enter para continuar ...")
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
        input("Presione enter para continuar ...")
    
    def consultar_programacion_sala(self):
        """
        Este método permite consultar la programación de una sala en específico, 
        mostrando todas las funciones programadas en la sala.
        """
        print("\nCONSULTA PROGRAMACIÓN DE SALA".center(40, "="))
        try:
            idSala = int(input("Ingrese el ID de la sala que desea consultar: "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        for i in range(self.cont_salas):
            if self.salas[i].id == idSala:
                self.salas[i].mostrar_programacion()
                input("Presione enter para continuar ...")
                return

        input(f"No se encontró ninguna sala con ID {idSala}. Presione enter para continuar ...")


    def consultar_funciones_pelicula(self):
        """
        Este método permite consultar las funciones programadas de una película específica,
        mostrando en qué salas y horarios se encuentra actualmente programada.
        """
        print("\nCONSULTA FUNCIONES DE UNA PELÍCULA".center(40, "="))
        peli = input("Ingrese el nombre de la película que desea buscar: ").strip()

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
                if prog.pelicula.nombreEsp.lower() == peli.lower():
                    print(f"Sala {self.salas[i].id} - Horario: {prog.horario}")
                    encontrada = True

        if not encontrada:
            input("La película no se encuentra programada actualmente. Presione enter para continuar ...")
            return
        input("Presione enter para continuar ...")
    
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
            input("Sala registrada con éxito. Presione enter para continuar ...")
        else:
            input("Ya no es posible crear más salas. Presione enter para continuar ...")

    def agregar_funcion(self):
        """
        Este método permite registrar una nueva función en una sala y horario específicos.
        """
        print("\nPROGRAMAR UNA NUEVA FUNCIÓN".center(40, "="))

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        try:
            idSala = int(input("Ingrese el ID de la sala en la que desea programar la función: "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        sala_pos = -1
        for i in range(self.cont_salas):
            if self.salas[i].id == idSala:
                sala_pos = i
                break

        if sala_pos == -1:
            input(f"No se encontró ninguna sala con ID {idSala}. Presione enter para continuar ...")
            return

        peli = input("Ingrese el nombre de la película que desea programar: ").strip()
        horario = input("Ingrese el horario (HH:MM) en el que desea programar: ").strip()
    
        # Buscar la película
        pelicula = None
        for i in range(self.cont_peliculas):
            if self.peliculas[i].nombreEsp.lower() == peli.lower():
                pelicula = self.peliculas[i]
                break

        if pelicula is None:
            input("No se encontró ninguna película con ese nombre. Presione enter para continuar ...")
            return

        # Validar traslape
        if not self.salas[sala_pos].validar_traslape(horario, pelicula.duracion):
            input("Ya existe una función programada a esa hora. Presione enter para continuar ...")
            return
        
        # Crear la función y asignarla
        filas = self.salas[sala_pos].filas
        asientos = self.salas[sala_pos].asientosFila
        funcion = Programacion(pelicula, horario, filas, asientos)
        self.salas[sala_pos].programacion[self.salas[sala_pos].cont_programacion] = funcion
        self.salas[sala_pos].cont_programacion += 1
        input("Función agregada con éxito. Presione enter para continuar ...")

    def eliminar_funcion(self):
        """
        Este método permite eliminar una funcion que esta programada en un horario de una sala en especifico.
        """
        print("\nELIMINAR FUNCIÓN".center(40, "="))

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        try:
            idSala = int(input("Ingrese el ID de la sala de la que desea eliminar la función: "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        sala_pos = -1
        for i in range(self.cont_salas):
            if self.salas[i].id == idSala:
                sala_pos = i
                break

        if sala_pos == -1:
            input(f"No se encontró ninguna sala con ID {idSala}. Presione enter para continuar ...")
            return

        horario = input("Ingrese el horario (HH:MM) de la función a eliminar: ").strip()

        sala = self.salas[sala_pos]
        for i in range(sala.cont_programacion):
            if sala.programacion[i].horario == horario:
                # Desplazar las funciones siguientes una posición a la izquierda
                for j in range(i, sala.cont_programacion - 1):
                    sala.programacion[j] = sala.programacion[j + 1]
                sala.programacion[sala.cont_programacion - 1] = None  # Limpia la última posición
                sala.cont_programacion -= 1
                input("Función eliminada con éxito. Presione enter para continuar ...")
                return

        input(f"No se encontró ninguna función en ese horario. Presione enter para continuar ...")


    def modificar_horario_funcion(self):
        """
        Este método permite modificar el horario de una función programada en una sala,
        validando que el nuevo horario no genere traslape con otras funciones en la misma sala.
        """
        print("\nMODIFICAR HORARIO DE FUNCIÓN".center(40, "="))

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar ...")
            return

        try:
            idSala = int(input("Ingrese el ID de la sala donde desea modificar la función: "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        sala_pos = -1
        for i in range(self.cont_salas):
            if self.salas[i].id == idSala:
                sala_pos = i
                break

        if sala_pos == -1:
            input(f"No se encontró ninguna sala con ID {idSala}. Presione enter para continuar ...")
            return

        horario_actual = input("Ingrese el horario actual (HH:MM) de la función: ").strip()

        sala = self.salas[sala_pos]
        for i in range(sala.cont_programacion):
            funcion = sala.programacion[i]
            if funcion.horario == horario_actual:
                nuevo_horario = input("Ingrese el nuevo horario (HH:MM) para la función: ").strip()
                duracion = funcion.pelicula.duracion

                if sala.validar_traslape(nuevo_horario, duracion, excluir=i):
                    funcion.horario = nuevo_horario
                    input("Horario modificado con éxito. Presione enter para continuar ...")
                else:
                    input("El nuevo horario genera un traslape con otra función. Presione enter para continuar ...")
                return

        input("No se encontró ninguna función en ese horario. Presione enter para continuar ...")
    
    def eliminar_funciones_pelicula(self, nombre_pelicula):
        """
        Elimina todas las funciones de todas las salas que correspondan a la película dada por nombre.
        """
        for i in range(self.cont_salas):
            sala = self.salas[i]
            j = 0
            while j < sala.cont_programacion:
                funcion = sala.programacion[j]
                if funcion.pelicula.nombreEsp.lower() == nombre_pelicula.lower():
                    # Eliminar la función desplazando las siguientes
                    for k in range(j, sala.cont_programacion - 1):
                        sala.programacion[k] = sala.programacion[k + 1]
                    sala.programacion[sala.cont_programacion - 1] = None
                    sala.cont_programacion -= 1
                else:
                    j += 1

    def realizar_reserva(self):
        """
        Este método permite realizar la reserva de asientos en una función en una sala especifica.
        """
        from datetime import date

        self.consultar_programacion_general()

        if self.cont_salas == 0:
            input("No hay salas registradas aún. Presione enter para continuar...")
            return

        try:
            idSala = int(input("Ingrese el número de la sala en la que desea reservar: "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        if idSala < 1 or idSala > self.cont_salas:
            input("Sala no válida. Presione enter para continuar...")
            return

        sala = self.salas[idSala - 1]

        if sala.cont_programacion == 0:
            input("La sala seleccionada no tiene funciones programadas. Presione enter para continuar...")
            return

        try:
            idFuncion = int(input("Ingrese el número de la función que desea reservar (según el orden mostrado): "))
        except ValueError:
            input("Debe ingresar un número válido. Presione enter para continuar ...")
            return

        if idFuncion < 1 or idFuncion > sala.cont_programacion:
            input("Función no válida. Presione enter para continuar...")
            return

        funcion = sala.programacion[idFuncion - 1]

        funcion.mostrar_disponibilidad()

        try:
            fila = input("Ingrese la fila en la que desea reservar: ").strip().upper()
            cantidad = int(input("Ingrese la cantidad de asientos que desea reservar: "))
        except ValueError:
            input("Debe ingresar una cantidad válida. Presione enter para continuar ...")
            return

        asientos = funcion.reservar_asientos(fila, cantidad)

        if type(asientos) == bool:
            input("No fue posible reservar asientos contiguos en esa fila. Presione enter para continuar...")
            return

        fechaVenta = date.today().strftime('%d-%m-%Y')
        peli = funcion.pelicula.nombreEsp
        horario = funcion.horario
        total = sala.valorBoleta * cantidad
        calificacion = funcion.pelicula.calificacion

        res = Reserva(fechaVenta, self.nombre, idSala, peli, horario, total, calificacion)

        for asiento in asientos:
            res.agregar_silla(asiento)

        self.reservas[self.cont_reservas] = res
        self.cont_reservas += 1

        res.generar_boleta()
        input("Reserva realizada con exito. Presione enter para continuar ...")

    def consultar_ocupacion(self):
        """
        Muestra todas las funciones de todas las salas ordenadas por porcentaje de ocupación, de mayor a menor.
        """
        print("\nOCUPACIÓN DE FUNCIONES POR SALA".center(40, "="))

        if self.cont_salas == 0:
            input("No hay salas registradas. Presione enter para continuar...")
            return

        max_funciones = 60  # máximo de funciones que podrían existir (ajustable)
        salas_ids = np.empty(max_funciones, dtype=int)
        nombres_pelis = np.empty(max_funciones, dtype=object)
        horarios = np.empty(max_funciones, dtype=object)
        ocupaciones = np.empty(max_funciones, dtype=float)

        cont = 0
        for i in range(self.cont_salas):
            sala = self.salas[i]
            for j in range(sala.cont_programacion):
                funcion = sala.programacion[j]
                salas_ids[cont] = sala.id
                nombres_pelis[cont] = funcion.pelicula.nombreEsp
                horarios[cont] = funcion.horario
                ocupaciones[cont] = funcion.consultar_ocupacion()
                cont += 1

        if cont == 0:
            input("No hay funciones programadas. Presione enter para continuar...")
            return

        # Ordenamiento por porcentaje de ocupación (burbuja)
        for i in range(cont - 1):
            for j in range(i + 1, cont):
                if ocupaciones[i] < ocupaciones[j]:
                    ocupaciones[i], ocupaciones[j] = ocupaciones[j], ocupaciones[i]
                    salas_ids[i], salas_ids[j] = salas_ids[j], salas_ids[i]
                    nombres_pelis[i], nombres_pelis[j] = nombres_pelis[j], nombres_pelis[i]
                    horarios[i], horarios[j] = horarios[j], horarios[i]

        print(f"{'Sala':<6}{'Película':<25}{'Horario':<10}{'Ocupación (%)'}")
        for i in range(cont):
            print(f"{salas_ids[i]:<6}{nombres_pelis[i]:<25}{horarios[i]:<10}{ocupaciones[i]:.2f}")
        input("Presione enter para continuar ...")

    def consultar_recaudo_sala(self):
        """
        Consulta el valor total recaudado por una sala en un periodo dado.
        """
        from datetime import datetime

        print("\nRECAUDO POR SALA".center(40, "="))
        try:
            idSala = int(input("Ingrese el ID de la sala: "))
            fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (AAAA-MM-DD): "), "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (AAAA-MM-DD): "), "%Y-%m-%d").date()
        except:
            input("Error en la entrada. Verifique el formato de la fecha o el ID. Presione enter para continuar ...")
            return

        sala_valida = any(self.salas[i].id == idSala for i in range(self.cont_salas))
        if not sala_valida:
            input("No se encontró la sala indicada. Presione enter para continuar...")
            return

        total = 0.0
        for i in range(self.cont_reservas):
            res = self.reservas[i]
            try:
                fecha_reserva = datetime.strptime(res.fechaVenta, "%d-%m-%Y").date()
                if res.idSala == idSala and fecha_inicio <= fecha_reserva <= fecha_fin:
                    total += res.precioTotal
            except:
                continue

        if total == 0.0:
            input("No hubo ingresos para esa sala en el periodo indicado. Presione enter para continuar...")
        else:
            print(f"Total recaudado por la sala {idSala}: ${total:,.2f}")
            input("Presione enter para continuar ...")

    def consultar_recaudo_total(self):
        """
        Consulta el valor total recaudado por el complejo en un periodo dado.
        """
        from datetime import datetime

        print("\nRECAUDO TOTAL DEL COMPLEJO".center(40, "="))
        try:
            fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (AAAA-MM-DD): "), "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(input("Ingrese la fecha de fin (AAAA-MM-DD): "), "%Y-%m-%d").date()
        except:
            input("Error en la entrada. Verifique el formato de las fechas. Presione enter para continuar ...")
            return

        total = 0.0
        for i in range(self.cont_reservas):
            res = self.reservas[i]
            try:
                fecha_reserva = datetime.strptime(res.fechaVenta, "%d-%m-%Y").date()
                if fecha_inicio <= fecha_reserva <= fecha_fin:
                    total += res.precioTotal
            except:
                continue

        if total == 0.0:
            input("No se registraron ingresos en ese periodo. Presione enter para continuar...")
        else:
            print(f"Total recaudado por el complejo en ese periodo: ${total:,.2f}")
            input("Presione enter para continuar ...")
    
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
        self.salas[0].programacion[0] = Programacion(peli,"11:30", sala.filas, sala.asientosFila)
        self.salas[0].cont_programacion += 1
        self.cont_salas = 1

        print("Datos de prueba cargados correctamente.")



App = AppComplejo()
App.cargar_datos_prueba()
App.ejecutar()