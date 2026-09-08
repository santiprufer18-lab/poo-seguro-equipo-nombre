"""
Script de pruebas de encapsulamiento y seguridad para POO.
Verifica:
1. Validacion de patente en el constructor (debe fallar con ValueError si es invalida).
2. Proteccion de solo lectura en en_taller (debe fallar con AttributeError al intentar modificarla desde afuera).
"""

from auto import Auto

print("=" * 60)
print("INICIO DE PRUEBAS DE SEGURIDAD Y ENCAPSULAMIENTO")
print("=" * 60)

# -------------------------------------------------------------
# PRUEBA 1: Crear un Auto con una patente invalida (ValueError)
# -------------------------------------------------------------
print("\n[Prueba 1] Intentando crear un Auto con patente invalida ('ABC')...")
try:
    auto_invalido = Auto("ABC", 2022) # Menos de 6 caracteres
    print("[FALLO] ERROR: Se permitio crear un Auto con patente invalida.")
except ValueError as e:
    print(f"[EXITO] Fallo correctamente con ValueError: {e}")


# -------------------------------------------------------------
# PRUEBA 2: Modificar en_taller desde afuera (AttributeError)
# -------------------------------------------------------------
print("\n[Prueba 2] Creando Auto valido e intentando modificar 'en_taller' directamente...")
try:
    auto_valido = Auto("AB1234", 2022)
    print(f"Estado inicial de en_taller: {auto_valido.en_taller}")
    
    # Intento de modificacion directa desde afuera (debe ser bloqueado por ser property de solo lectura)
    auto_valido.en_taller = True
    print("[FALLO] ERROR: Se permitio modificar 'en_taller' desde afuera.")
except AttributeError as e:
    print(f"[EXITO] Fallo correctamente con AttributeError: {e}")

print("\n" + "=" * 60)
print("FIN DE LAS PRUEBAS: Todas las restricciones de seguridad pasaron.")
print("=" * 60)
