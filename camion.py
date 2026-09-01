from vehiculo import Vehiculo # Importa la clase base Vehiculo


class Camion(Vehiculo): # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, anio y capacidad_carga (en kilos)
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga en kilos como atributo privado
