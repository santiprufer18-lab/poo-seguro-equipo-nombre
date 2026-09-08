from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Moto(Vehiculo): # Define la clase Moto heredando de Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para Moto
        return 15000 # Retorna la tarifa específica de 15000 como entero
