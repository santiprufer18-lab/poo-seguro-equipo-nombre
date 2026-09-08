from auto import Auto

# =========================================================================
# PRUEBA 1: Crear un Auto con una patente inválida
# Debe fallar con ValueError porque no cumple con el mínimo de 6 caracteres.
# =========================================================================
print("--- PRUEBA 1: Intentando crear un Auto con patente inválida ('ABC') ---")
try:
    auto_invalido = Auto("ABC", 2022)
    print("ERROR: La validación no funcionó, se permitió crear el objeto.")
except ValueError as e:
    print(f"CAPTURA EXITOSA (ValueError): {e}")


# =========================================================================
# PRUEBA 2: Modificar el atributo en_taller desde afuera de la clase
# Debe fallar con AttributeError porque en_taller es una property de solo lectura.
# =========================================================================
print("\n--- PRUEBA 2: Intentando modificar en_taller desde afuera de la clase ---")
try:
    auto_valido = Auto("AB1234", 2022)
    print(f"Estado original de en_taller: {auto_valido.en_taller}")
    
    # Intento de modificación directa desde afuera
    auto_valido.en_taller = True
    print("ERROR: La protección falló, se permitió modificar en_taller.")
except AttributeError as e:
    print(f"CAPTURA EXITOSA (AttributeError): {e}")

print("\nTodas las pruebas de seguridad y encapsulamiento finalizaron correctamente.")
