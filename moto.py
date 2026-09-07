from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Moto(Vehiculo): # Define la clase Moto heredando de Vehiculo
    def tarifa_hora(self) -> int: # Método que sobrescribe la tarifa por hora para Moto
        return 15000 # Retorna un valor fijo de 15000 para moto
