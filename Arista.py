class Arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __str__(self):
        return f"{self.origen} - {self.destino} - Peso: {self.peso}"