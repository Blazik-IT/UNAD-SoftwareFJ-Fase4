from clases import Cliente, ReservaSala, AlquilerEquipo, Asesoria
from gestion import Reserva
import logging

def ejecutar_simulacion():
    print("--- Iniciando Sistema Software FJ ---")
    clientes = []
    
    # 10 Operaciones mixtas (Válidas e Inválidas) 
    operaciones = [
        ("C", "101", "Juan Perez"),          # 1. Registro válido
        ("C", "ABC", "Error User"),         # 2. Registro inválido (ID no numérico)
        ("S", "Sala A", 100, "SALA"),       # 3. Servicio válido
        ("S", "Equipo X", 200, "EQUIPO"),   # 4. Servicio válido
        ("S", "Asesoría Y", 300, "ASESORIA"),# 5. Servicio válido
        ("R", 0, 0, 2),                     # 6. Reserva exitosa (Cliente 1 + Sala)
        ("R", 0, 2, 1),                     # 7. Reserva exitosa (Cliente 1 + Asesoría)
        ("R", "ERROR", 0, 1),               # 8. Reserva fallida (Objeto incorrecto)
        ("C", "102", "Marta Gomez"),        # 9. Registro válido
        ("R", 1, 1, 5)                      # 10. Reserva exitosa
    ]

    servicios = []
    
    for i, op in enumerate(operaciones):
        print(f"Ejecutando Operación {i+1}...")
        try:
            if op[0] == "C":
                c = Cliente(op[1], op[2])
                clientes.append(c)
                print(f"  OK: Cliente registrado.")
            elif op[0] == "S":
                if op[3] == "SALA": s = ReservaSala(op[1], op[2])
                elif op[3] == "EQUIPO": s = AlquilerEquipo(op[1], op[2])
                else: s = Asesoria(op[1], op[2])
                servicios.append(s)
                print(f"  OK: Servicio creado.")
            elif op[0] == "R":
                res = Reserva(clientes[op[1]], servicios[op[2]], op[3])
                print(f"  OK: {res.procesar_reserva()}")
        
        except Exception as e: # Manejo robusto de errores [cite: 17, 18]
            logging.error(f"Operación {i+1} falló: {e}")
            print(f"  ERROR CONTROLADO: {e}. El sistema continúa...")

if __name__ == "__main__":
    ejecutar_simulacion()
    print("\n--- Simulación finalizada. Revise 'registro_eventos.log' para detalles. ---")
