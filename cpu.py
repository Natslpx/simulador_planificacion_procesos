import time

from proceso import Proceso


class CPU:
    def __init__(self, id):
        self.id = id
        self.procesos = []  # Cola de procesos asignados
        self.algorithm = "FCFS"  # Algoritmo por defecto
        self.quantum = None  # Quantum solo aplicable a Round Robin

    def limpiar_procesos(self):
        self.procesos = []

    def asignar_proceso(self, proceso):
        self.procesos.append(proceso)
