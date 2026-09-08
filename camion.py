from vehiculo import Vehiculo # Importa la clase base Vehiculo desde el módulo vehiculo

class Camion(Vehiculo): # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, año y capacidad de carga
        super().__init__(patente, anio) # Invoca al constructor de la clase padre (Vehiculo) para inicializar patente y año
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga en kilos como atributo privado

    @property
    def capacidad_carga(self) -> int: # Getter para acceder de forma segura a la capacidad de carga
        return self.__capacidad_carga # Retorna el valor del atributo privado __capacidad_carga

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para Camion
        return 40000 # Retorna la tarifa específica de 40000 como entero
