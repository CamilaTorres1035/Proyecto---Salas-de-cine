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
    
    def consultar_ocupacion(self):
        pass
    
    def mostrar_disponibilidad(self):
        pass
    
    def verificar_contiguos(self):
        pass
    
    def reservar_asientos(self):
        pass