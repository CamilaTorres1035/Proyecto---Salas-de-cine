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

    def mostrar_programacion(self):
        print(f"\nProgramación de la Sala {self.id}:")
        if self.cont_programacion == 0:
            print("No hay funciones programadas en esta sala.")
        else:
            for i in range(self.cont_programacion):
                print(f"{i+1}. Película: {self.programacion[i].pelicula.nombreEsp} - Horario: {self.programacion[i].horario}")
    
    def pedir_datos(self):
        while True:
            try:
                self.valorBoleta = float(input("Ingrese el valor de la boleta para la sala: "))
                if self.valorBoleta > 0: break
                print("El valor de la boleta debe ser mayor a 0.")
            except ValueError:
                print("El valor de la boleta debe ser un número válido.")
        
        while True:
            try:
                self.filas = int(input("Ingresa el número de filas de la sala: "))
                if self.filas > 0: break
                print("El número de filas no puede ser menor a 1.")
            except ValueError:
                print("Debe ingresar un número entero válido.")
        
        while True:
            try:
                self.asientosFila = int(input("Ingresa el número de asientos por fila: "))
                if 0 < self.asientosFila <= 22: break
                print("El número de asientos debe estar entre 1 y 22.")
            except ValueError:
                print("Debe ingresar un número entero válido.")
    
    def validar_traslape(self, horario, duracion, excluir=-1):
        """
        Verifica si un nuevo horario se traslapa con alguna función ya programada en la sala,
        considerando la duración de la función. Se puede excluir una posición de comparación 
        (por ejemplo, al modificar el horario de una función ya existente).

        Parámetros:
            horario (str): Horario propuesto en formato HH:MM.
            duracion (int): Duración de la nueva función en minutos.
            excluir (int): Índice opcional para excluir una función existente (por defecto -1, sin excluir).

        Retorna:
            bool: True si NO hay traslape, False si SÍ hay traslape.
        """
        h, m = map(int, horario.split(":"))
        inicio = h * 60 + m
        fin = inicio + duracion

        for i in range(self.cont_programacion):
            if i == excluir:
                continue

            prog = self.programacion[i]
            h_prog, m_prog = map(int, prog.horario.split(":"))
            inicio_prog = h_prog * 60 + m_prog
            fin_prog = inicio_prog + prog.pelicula.duracion

            if inicio < fin_prog and fin > inicio_prog:
                return False  # Traslape detectado

        return True  # No hay traslapes
    
    def consultar_recaudo(self):
        """
        Calcula el total de dinero recaudado por la sala, sumando el valor de las boletas
        vendidas en todas las funciones programadas.
    
        Retorna:
            float: Total de dinero recaudado.
        """
        total = 0.0
        total_asientos = self.filas * self.asientosFila
    
        for i in range(self.cont_programacion):
            prog = self.programacion[i]
            ocupacion = prog.consultar_ocupacion()  # % ocupación
            ocupados = (ocupacion / 100) * total_asientos
            total += ocupados * self.valorBoleta
    
        return total

