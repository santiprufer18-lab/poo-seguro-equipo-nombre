from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from auto import Auto # Importa la clase Auto desde el archivo local auto.py
from moto import Moto # Importa la clase Moto desde el archivo local moto.py
from camion import Camion # Importa la clase Camion desde el archivo local camion.py

# Instanciación de objetos
vehiculo_base = Vehiculo("BASE01", 2015) # Instancia un objeto Vehiculo base
auto = Auto("AB1234", 2018, 200) # Instancia un objeto Auto con capacidad de maletero
moto = Moto("CD5678", 2020) # Instancia un objeto Moto
camion = Camion("EF9012", 2023, 5000) # Instancia un objeto Camion con capacidad de carga

# Pruebas de ingreso al taller
print(auto.ingresar()) # Ejecuta ingresar() del auto
print(moto.ingresar()) # Ejecuta ingresar() de la moto
print(camion.ingresar()) # Ejecuta ingresar() del camión

# Pruebas de encapsulamiento y asignación de patente
pruebaEnc = camion.patente # Obtiene la patente del camión
camion.set_patente("EF9012") # Asigna una nueva patente válida usando el método setter
print(f"Patente obtenida: {pruebaEnc}") # Imprime la patente obtenida


# Pruebas de tarifa_hora()
print(f"Tarifa por hora Vehiculo Base: ${vehiculo_base.tarifa_hora()}") # Tarifa base (5000)
print(f"Tarifa por hora Auto: ${auto.tarifa_hora()}") # Tarifa sobreescrita Auto (25000)
print(f"Tarifa por hora Moto: ${moto.tarifa_hora()}") # Tarifa sobreescrita Moto (15000)
print(f"Tarifa por hora Camión: ${camion.tarifa_hora()}") # Tarifa sobreescrita Camion (40000)
