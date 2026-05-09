from abc import ABC, abstractmethod
import logging

# Configuración del archivo de logs (requisito del sistema) 
logging.basicConfig(filename='registro_eventos.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class EntidadBase(ABC):
    """Clase abstracta que representa entidades generales [cite: 21]"""
    @abstractmethod
    def obtener_detalles(self):
        pass

class Cliente(EntidadBase):
    """Clase Cliente con encapsulación y validaciones [cite: 22]"""
    def __init__(self, id_cliente, nombre):
        if not str(id_cliente).isdigit():
            raise ValueError("ID de cliente debe ser numérico") # Excepción [cite: 19]
        self.__id_cliente = id_cliente # Atributo privado (encapsulación)
        self.__nombre = nombre

    def obtener_detalles(self):
        return f"Cliente: {self.__nombre} (ID: {self.__id_cliente})"

class Servicio(ABC):
    """Clase abstracta Servicio [cite: 23]"""
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, impuestos=0.19): # Sobrecarga mediante parámetros [cite: 26]
        pass

class ReservaSala(Servicio):
    """Servicio especializado 1 [cite: 24]"""
    def calcular_costo(self, impuestos=0.19):
        return self.precio_base * (1 + impuestos)

class AlquilerEquipo(Servicio):
    """Servicio especializado 2 [cite: 24]"""
    def calcular_costo(self, impuestos=0.19):
        return (self.precio_base + 50) * (1 + impuestos) # Costo extra por mantenimiento

class Asesoria(Servicio):
    """Servicio especializado 3 [cite: 24]"""
    def calcular_costo(self, impuestos=0.19):
        return self.precio_base * (1 + impuestos) * 0.90 # 10% de descuento
