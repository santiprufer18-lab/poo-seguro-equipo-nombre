from vehiculo import Vehiculo # Importa la clase base Vehiculo


class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cilindrada: int): # Constructor que recibe patente, anio y cilindrada (en cc)
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__cilindrada: int = cilindrada # Guarda la cilindrada en cc como atributo privado
