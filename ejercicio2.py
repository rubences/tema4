import heapq

class Mision:
    def __init__(self, tipo, reino_destino, dios):
        self.tipo = tipo
        self.reino_destino = reino_destino
        self.dios = dios
        self.prioridad = 0 if dios in ['Odín', 'Loki'] else 1

    def asignar_recursos(self):
        # Aquí se puede implementar la lógica para asignar recursos basado en el tipo y la prioridad de la misión
        pass

    def __lt__(self, other):
        return self.prioridad < other.prioridad

class GestorMisiones:
    def __init__(self):
        self.misiones = []

    def agregar_mision(self, mision):
        heapq.heappush(self.misiones, mision)

    def mostrar_misiones(self):
        while self.misiones:
            mision = heapq.heappop(self.misiones)
            print(f'Tipo: {mision.tipo}, Reino destino: {mision.reino_destino}, Dios: {mision.dios}, Prioridad: {"alta" if mision.prioridad == 0 else "baja"}')