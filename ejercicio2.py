import heapq



class Mision:
    def __init__(self, tipo, reino_destino, dios):
        self.tipo = tipo
        self.reino_destino = reino_destino
        self.dios = dios
        self.prioridad = 0 if dios in ['Odín', 'Loki'] else 1
        self.valkirias = 0
        self.unidades = 0

    def asignar_recursos(self):
        if self.tipo == "defensa":
            if self.prioridad == 0:
                self.valkirias = 10
                self.unidades = 100
            else:
                self.valkirias = 5
                self.unidades = 50
        elif self.tipo == "exploración":
            if self.prioridad == 0:
                self.valkirias = 8
                self.unidades = 80
            else:
                self.valkirias = 4
                self.unidades = 40
        elif self.tipo == "conquista":
            if self.prioridad == 0:
                self.valkirias = 12
                self.unidades = 120
            else:
                self.valkirias = 6
                self.unidades = 60
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

if __name__ == "__main__":
    gestor = GestorMisiones()

    while True:
        print("1. Agregar misión")
        print("2. Mostrar misiones")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            tipo = input("Ingrese el tipo de misión: ")
            reino_destino = input("Ingrese el reino destino: ")
            dios = input("Ingrese el dios que solicitó la misión: ")
            mision = Mision(tipo, reino_destino, dios)
            gestor.agregar_mision(mision)
        elif opcion == 2:
            gestor.mostrar_misiones()
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intente de nuevo.")