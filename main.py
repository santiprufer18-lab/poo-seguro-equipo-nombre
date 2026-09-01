from vehiculo import Vehiculo # Importa la clase base Vehiculo
from auto import Auto # Importa la clase Auto desde auto.py
from moto import Moto # Importa la clase Moto desde moto.py
from camion import Camion # Importa la clase Camion desde camion.py

auto1 = Auto("AB1234", 2020, 4) # Instancia un objeto Auto con patente, año y cantidad de puertas
moto1 = Moto("CD5678", 2022, 250) # Instancia un objeto Moto con patente, año y cilindrada (cc)
camion1 = Camion("EF9012", 2019, 8000) # Instancia un objeto Camion con patente, año y capacidad de carga (kg)

print(auto1.ingresar()) # Registra el ingreso del auto al taller y muestra el resultado
print(moto1.ingresar()) # Registra el ingreso de la moto al taller y muestra el resultado
print(camion1.ingresar()) # Registra el ingreso del camión al taller y muestra el resultado

print(f"Tarifa por hora del auto: ${auto1.tarifa_hora()}") # Imprime la tarifa por hora del auto
print(f"Tarifa por hora de la moto: ${moto1.tarifa_hora()}") # Imprime la tarifa por hora de la moto
print(f"Tarifa por hora del camión: ${camion1.tarifa_hora()}") # Imprime la tarifa por hora del camión
