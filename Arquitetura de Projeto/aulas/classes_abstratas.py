from abc import ABC, abstractmethod

class sensorRemoto(ABC): #classes abstratas faz uma interface em python
    @abstractmethod
    def aumentar_volume(self):
        pass

    @abstractmethod
    def diminuir_volume(self):
        pass

class FabricanteA(sensorRemoto):
    def aumentar_volume(self):
        print("Aumentar volume fabricante A")

    def diminuir_volume(self):
        print("diminuir volume fabricante A")

class ControleRemoto:
    def __init__(self):
        sensor = FabricanteA()

    def aumentar_volume(self):
        sensor.aumentar_volume()

controle = ControleRemoto()
controle.aumentar_volume()