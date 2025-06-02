class Pelicula:
    """
    Esta clase representa una película que puede ser programada en una o varias salas.
    Almacena toda la información descriptiva y de estado de la película.
    
    Atributos:
        nombreEsp: cadena que representa el nombre de la pelicula en español.
        nombreOriginal: cadena que representa el nombre original de la pelicula.
        anioEstreno: entero que representa el año en que se estreno la pelicua.
        duracion: entero que indica la duracion en minutos de la pelicula.
        genero: cadena que indica a que genero pertenece la pelicula (drama, suspenso, terror, acción, comedia o infantil)
        paisOrigen: cadena que indica el pais de oriden de la pelicula.
        estado: entero que representa el estado de la pelicula (1: activo, 0: inactivo)
        calificacion: real que representa la calificacion que tiene la pelicula
    
    Constantes:
        ESTADO_ACTIVO: constante con valor 1 que representa el estado activo.
        ESTADO_INACTIVO: constante con valor 0 que representa el estado inactivo.
    
    Autor: Valeria Hernandez
    Fecha de creación: 30/05/2024
    """
    nombreEsp = str
    nombreOriginal = str
    anioEstreno = int
    duracion = int
    genero = str
    paisOrigen = str
    estado = int
    calificacion = float
    
    ESTADO_ACTIVO = 1
    ESTADO_INACTIVO = 0
    
    def __init__(self, nombreEsp = "", nombreOriginal = "", anioEstreno = 0, duracion = 0, genero = "", paisOrigen = "", calificacion = 0.0):
        self.nombreEsp = nombreEsp
        self.nombreOriginal = nombreOriginal
        self.anioEstreno = anioEstreno
        self.duracion = duracion
        self.genero = genero
        self.paisOrigen = paisOrigen
        self.estado = self.ESTADO_ACTIVO
        self.calificacion = calificacion
    
    def pedir_datos(self):
        """
        Este método solicita al usuario los datos de una nueva película por consola.
        """
        from datetime import datetime
        anio_actual = datetime.now().year

        while True:
            self.nombreEsp = input("Ingrese el nombre de la película en español: ").strip()
            if self.nombreEsp: break
            print("El nombre de la película no puede estar vacío.")
        
        while True:
            self.nombreOriginal = input("Ingrese el nombre original de la película: ").strip()
            if self.nombreOriginal: break
            print("El nombre de la película no puede estar vacío.")

        while True:
            try:
                self.anioEstreno = int(input("Ingrese el año de estreno: "))
                if 1900 <= self.anioEstreno <= anio_actual:
                    break
                print(f"El año debe estar entre 1900 y {anio_actual}")
            except ValueError:
                print("El año debe ser un número entero válido.")

        while True:
            try:
                self.duracion = int(input("Ingrese la duración en minutos: "))
                if self.duracion > 0:
                    break
                print("La duración debe ser mayor que 0.")
            except ValueError:
                print("Debe ingresar un número entero.")

        while True:
            self.genero = input("Ingrese el género de la película: ").strip()
            if self.genero: break
            print("El genero de la película no puede estar vacío.")
        
        while True:
            self.paisOrigen = input("Ingrese el país de origen: ").strip()
            if self.paisOrigen: break
            print("El país de orígen de la película no puede estar vacío.")

        while True:
            try:
                self.calificacion = float(input("Ingrese la calificación de la película (0.0 - 5.0): "))
                if 0.0 <= self.calificacion <= 5.0:
                    break
                print("La calificación debe estar entre 0.0 y 5.0.")
            except ValueError:
                print("Debe ingresar un número real válido.")
    
    def cambiar_estado(self, nuevo_estado):
        """
        Este metodo sirve para cambiar el estado de una pelicula entre activo o inactivo.

        Parametros:
        nuevo_estado: Nuevo estado de la pelicula.
        """
        if nuevo_estado in (self.ESTADO_ACTIVO, self.ESTADO_INACTIVO):
            self.estado = nuevo_estado
            return True
        print("El estado ingresado es invalido")
        return False
    
    def mostrar_detalle(self):
        """
        Este método muestra en pantalla la información completa de la película.
        """
        print("\nDETALLE DE LA PELÍCULA".center(40, "-"))
        print(f"Nombre en español: {self.nombreEsp}")
        print(f"Nombre original: {self.nombreOriginal}")
        print(f"Año de estreno: {self.anioEstreno}")
        print(f"Duración: {self.duracion} minutos")
        print(f"Género: {self.genero}")
        print(f"País de origen: {self.paisOrigen}")
