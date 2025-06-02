import numpy as np

class Reserva:
    """
    Clase que representa una reserva de boletas realizada por un cliente para una función específica en una sala del complejo.

    ATRIBUTOS:
        fechaVenta: cadena con la fecha en que se realizó la reserva (formato AAAA-MM-DD).
        nombreComplejo: cadena con el nombre del complejo de cine donde se realiza la reserva.
        idSala: entero que identifica la sala donde se hará la función.
        nombrePelicula: cadena con el nombre de la película reservada.
        horario: cadena que representa el horario de la función (formato HH:MM).
        precioTotal: real que indica el precio total pagado por la reserva.
        calificacionPelicula: real que represnta la calificacion que tiene la pelicula.
        sillasReservadas: arreglo de cadenas que contiene los identificadores de los asientos reservados (máximo 22).
        cont_sillas: contador que indica cuantas sillas han sido asignadas.

    Autor: Valeria Hernandez
    Fecha de creación: 31/05/2024
    """
    
    fechaVenta = str
    nombreComplejo = str
    idSala = int
    nombrePelicula = str
    horario = str
    precioTotal = float
    calificacionPelicula = float
    sillasReservadas = np.ndarray
    cont_sillas = int
    
    def __init__(self, fechaVenta="", nombreComplejo="", idSala=0, nombrePelicula="", horario="", precioTotal=0.0, calificacionPelicula=0.0):
        self.fechaVenta = fechaVenta
        self.nombreComplejo = nombreComplejo
        self.idSala = idSala
        self.nombrePelicula = nombrePelicula
        self.horario = horario
        self.precioTotal = precioTotal
        self.calificacionPelicula = calificacionPelicula
        self.sillasReservadas = np.empty(22, dtype=object)
        self.cont_sillas = 0
    
    def agregar_silla(self, codigo_silla):
        pass

    def generar_boleta(self):
        pass