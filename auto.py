from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la clase Auto heredando de Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para Auto
        return 25000 # Retorna la tarifa específica de 25000 como entero
