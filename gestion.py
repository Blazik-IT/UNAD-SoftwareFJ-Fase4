import logging
from clases import Cliente, Servicio

class Reserva:
    """Clase Reserva que integra cliente, servicio y estado [cite: 25]"""
    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise TypeError("Datos de cliente o servicio inválidos")
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar_reserva(self):
        try:
            costo = self.servicio.calcular_costo()
            self.estado = "Confirmada"
            logging.info(f"Reserva exitosa para {self.cliente.obtener_detalles()}. Costo: {costo}")
            return f"Reserva Procesada. Total: {costo}"
        except Exception as e:
            logging.error(f"Error al procesar reserva: {e}")
            raise
