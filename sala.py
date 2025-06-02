import numpy as np

class Sala:
    """
    Esta clase representa una sala de cine dentro del complejo. Almacena su configuración
    de filas, asientos y programación semanal.

    Atributos:
        id: Entero que representa el identificador único de la sala.
        valorBoleta: Real que representa el precio por boleta de la sala.
        filas: Entero que representa el número de filas de asientos en la sala.
        asientosFila: Entero que representa la cantidad de asientos por fila.
        programacion: Arreglo con las funciones programadas en la sala.
        cont_programacion: contador que indica cuántas funciones han sido programadas.
    
    autor: Camila Torres
    Fecha de creación: 30/05/2024
    """
    id = int
    valorBoleta = float
    filas = int
    asientosFila = int
    programacion = np.ndarray
    cont_programacion = int

    def __init__(self, id = 0, valorBoleta = 0.0, filas = 0, asientosFila = 0):
        self.id = id
        self.valorBoleta = valorBoleta
        self.filas = filas
        self.asientosFila = asientosFila
        self.programacion = np.empty(5, dtype=object)
        self.cont_programacion = 0

    def pedir_datos(self):
        pass
    
    def validar_traslape(self):
        pass
    
    def consultar_recaudo(self):
        pass
    
    def mostrar_programacion(self):
        pass
