from vehiculo import Vehiculo # Importa la clase base Vehiculo


class Auto(Vehiculo): # Define la clase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cantidad_puertas: int): # Constructor que recibe patente, anio y cantidad_puertas
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__cantidad_puertas: int = cantidad_puertas # Guarda la cantidad de puertas como atributo privado
