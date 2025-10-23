class Vehiculo:
    vehiculosCreados = []
    kilometrosTotales = 0
    kilometrosRecorridos = 0

    def __init__(self, vehiculosCreados, KilometrosTotales, KilometrosRecorridos):
        self.vehiculosCreados = vehiculosCreados
        self.kilometrosTotales = KilometrosTotales
        self.kilometrosRecorridos = KilometrosRecorridos

    

class Bicicleta(Vehiculo):
    pass

class Coche(Vehiculo):
    pass
