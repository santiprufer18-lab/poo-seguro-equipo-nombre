# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

### 31 de Agosto de 2026
- **Creación de Subclases con Herencia:**
  - Se crearon e implementaron las clases `Auto` (`auto.py`), `Moto` (`moto.py`) y `Camion` (`camion.py`), todas heredando de la clase base `Vehiculo`.
- **Implementación de Constructores y `super()`:**
  - Se implementó en cada subclase su propio método constructor `__init__`, reutilizando la inicialización de `patente` y `anio` mediante la invocación a la superclase con `super().__init__(patente, anio)`.
- **Atributos Propios Encapsulados (Tipo `int`):**
  - **`Auto`:** Se definió el atributo privado `__cantidad_puertas: int` (número de puertas).
  - **`Moto`:** Se definió el atributo privado `__cilindrada: int` (cilindrada en cc).
  - **`Camion`:** Se definió el atributo privado `__capacidad_carga: int` (capacidad de carga en kilos).
- **Documentación y Buenas Prácticas:**
  - Se añadieron comentarios explicativos en cada línea de los archivos `auto.py`, `moto.py` y `camion.py`.
- **Control de Versiones:**
  - Publicación y sincronización de los avances en la rama `feature/desarrollo` en GitHub.
