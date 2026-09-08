from auto import Auto # Importa la clase Auto desde auto.py
from moto import Moto # Importa la clase Moto desde moto.py
from camion import Camion # Importa la clase Camion desde camion.py

# Creación de las instancias de Auto, Moto y Camion
auto = Auto("AB1234", 2018)
moto = Moto("CD5678", 2020)
camion = Camion("EF9012", 2023, 5000)

# Agrupación de los vehículos en una lista
vehiculos = [auto, moto, camion]

# Recorrido polimórfico: se invoca tarifa_hora() en cada objeto sin verificar su tipo o clase
for vehiculo in vehiculos:
    print(f"Vehículo patente {vehiculo.patente} -> Tarifa por hora: ${vehiculo.tarifa_hora()}")
