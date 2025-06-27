import numpy as np
from pelicula import Pelicula

class Programacion:
    """
    Esta clase representa una función programada en una sala, vinculando una película,
    un horario específico y el mapa de asientos disponibles.

    ATRIBUTOS:
        pelicula: Objeto de tipo Pelicula que se proyecta.
        horario: cadena que representa el horario de la función (formato HH:MM).
        asientos: Matriz bidimensional de enteros que representa el estado de los asientos (0 = disponible, 1 = reservado).
    
    autor: Camila Torres
    Fecha de creación: 31/05/2024
    """
    
    pelicula = Pelicula
    horario = str
    asientos = np.ndarray
    
    DISPONIBLE = 0
    RESERVADO = 1
    
    def __init__(self, pelicula, horario, filas = 0, asientoFila = 0):
        if filas <= 0 or asientoFila <= 0:
            raise ValueError("La cantidad de filas y asientos por fila debe ser mayor que cero.")
        self.pelicula = pelicula
        self.horario = horario
        self.asientos = np.full((filas, asientoFila), fill_value=self.DISPONIBLE)

    def mostrar_disponibilidad(self):
        """
        Muestra por consola el estado de los asientos de la función.
        0 = disponible, 1 = reservado.
        """
        import string  # Importa el módulo string para obtener letras del alfabeto
        self.letras = string.ascii_uppercase[:len(self.asientos)]  # Obtiene las primeras letras del alfabeto
        cad = "  "
        for i in range(len(self.asientos[0])):
            cad += str(i+1) +"  "
        print(cad)
        for i in range(len(self.asientos)):
            cad = self.letras[i] + " "
            for j in range(len(self.asientos[0])):
                if j > 8:    
                    cad += str(self.asientos[i][j]) + "   "
                    continue
                cad += str(self.asientos[i][j]) + "  "
            print(cad)
    
    def verificar_contiguos(self, idFila, cantidad):
        """
        Verifica si existen 'cantidad' de asientos contiguos disponibles en la fila dada.
        """
        fila = self.letras.index(idFila)
        total_asientos = len(self.asientos[0])
    
        for i in range(total_asientos - cantidad + 1):
            disponibles = True
            for j in range(cantidad):
                if self.asientos[fila][i + j] == self.RESERVADO:
                    disponibles = False
                    break
            if disponibles:
                return i  # Encontró un bloque contiguo disponible
    
        return -1  # No hay asientos contiguos disponibles

    def reservar_asientos(self, idFila, cantidad):
        idFila = str(idFila).upper()
        if idFila not in self.letras:
            input("Esa fila no existe en esta sala. Presione enter para continuar...")
            return False

        fila = self.letras.index(idFila)
        asientos = np.full((cantidad), fill_value="", dtype='<U10')
        
        inicio = self.verificar_contiguos(idFila, cantidad)
        
        if inicio == -1:
            input("No hay asientos contiguos disponibles en esa fila. Presione enter para continuar...")
            return False
        
        for i in range(cantidad):
            self.asientos[fila][inicio + i] = self.RESERVADO
            asientos[i] = f"{idFila}{inicio + i + 1}"
        
        return asientos

    def consultar_ocupacion(self):
        pass