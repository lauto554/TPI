import csv

from utils import mostrar_titulo


RUTA_ARCHIVO = "paises.csv"
CAMPOS_PAIS = ["nombre", "poblacion", "superficie", "continente"]


######################### CSV #########################
def cargar_paises():
    paises = []
    try:
        with open(RUTA_ARCHIVO, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip(),
                }
                paises.append(pais)
    except FileNotFoundError:
        print("Archivo CSV no encontrado. Se inicia con lista vacía.")
    except (KeyError, ValueError) as e:
        print(f"Error al leer el CSV: {e}")
    return paises


def guardar_paises(paises):
    try:
        with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PAIS)
            escritor.writeheader()
            escritor.writerows(paises)
        print("Cambios guardados correctamente.")
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")


########################## ABM #########################
def listar_paises(paises):
    mostrar_titulo("Listado de países")

    if not paises:
        print("No hay países cargados.")
        return

    print(f"{'Nombre':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<15}")
    print("-" * 75)
    for pais in paises:
        print(
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>15,} "
            f"{pais['superficie']:>18,} "
            f"{pais['continente']:<15}"
        )
    print(f"\nTotal: {len(paises)} país/es.")


def agregar_pais(paises):
    mostrar_titulo("Agregar país")

    nombre = _pedir_texto("Nombre del país: ")
    if nombre is None:
        return

    # No permitir duplicados
    if _buscar_por_nombre_exacto(paises, nombre) is not None:
        print(f"Ya existe un país con el nombre '{nombre}'.")
        return

    poblacion = _pedir_entero_positivo("Población: ")
    if poblacion is None:
        return

    superficie = _pedir_entero_positivo("Superficie (km²): ")
    if superficie is None:
        return

    continente = _pedir_texto("Continente: ")
    if continente is None:
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(pais)
    print(f"País '{nombre}' agregado. Recuerde guardar los cambios.")


def modificar_pais(paises):
    mostrar_titulo("Modificar país")

    if not paises:
        print("No hay países cargados.")
        return

    nombre = _pedir_texto("Nombre del país a modificar: ")
    if nombre is None:
        return

    pais = _buscar_por_nombre_exacto(paises, nombre)
    if pais is None:
        print(f"No se encontró el país '{nombre}'.")
        return

    print(f"\nDatos actuales → Población: {pais['poblacion']:,}  |  Superficie: {pais['superficie']:,} km²")

    nueva_poblacion = _pedir_entero_positivo("Nueva población (Enter para mantener): ", opcional=True)
    nueva_superficie = _pedir_entero_positivo("Nueva superficie (Enter para mantener): ", opcional=True)

    if nueva_poblacion is not None:
        pais["poblacion"] = nueva_poblacion
    if nueva_superficie is not None:
        pais["superficie"] = nueva_superficie

    print(f"País '{nombre}' actualizado. Recuerde guardar los cambios.")


def eliminar_pais(paises):
    mostrar_titulo("Eliminar país")

    if not paises:
        print("No hay países cargados.")
        return

    nombre = _pedir_texto("Nombre del país a eliminar: ")
    if nombre is None:
        return

    pais = _buscar_por_nombre_exacto(paises, nombre)
    if pais is None:
        print(f"No se encontró el país '{nombre}'.")
        return

    confirmacion = input(f"¿Confirma eliminar '{nombre}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        paises.remove(pais)
        print(f"País '{nombre}' eliminado. Recuerde guardar los cambios.")
    else:
        print("Operación cancelada.")


######################### HELPERS #########################
def _buscar_por_nombre_exacto(paises, nombre):
    nombre_lower = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_lower:
            return pais
    return None


def _pedir_texto(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        print("El campo no puede estar vacío.")
        return None
    return valor


def _pedir_entero_positivo(mensaje, opcional=False):
    texto = input(mensaje).strip()
    if not texto:
        if opcional:
            return None
        print("El campo no puede estar vacío.")
        return None
    if not texto.isdigit() or int(texto) <= 0:
        print("Debe ingresar un número entero mayor a 0.")
        return None
    return int(texto)
