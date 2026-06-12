import csv
import unicodedata

import questionary
from functions.utils import lista_vacia, mostrar_exito, mostrar_titulo, formatear_texto, buscar_por_nombre_exacto, pedir_nombre, pedir_continente, pedir_entero_positivo


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
        print("Archivo CSV no encontrado. Se inicia con lista vacia.")
    except (KeyError, ValueError) as e:
        print(f"Error al leer el CSV: {e}")
    return paises


def guardar_paises(paises):
    try:
        with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PAIS)
            escritor.writeheader()
            for pais in paises:
                fila = {
                    "nombre": formatear_texto(pais["nombre"]).title(),
                    "poblacion": pais["poblacion"],
                    "superficie": pais["superficie"],
                    "continente": formatear_texto(pais["continente"]).title(),
                }
                escritor.writerow(fila)
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")


########################## ABM #########################
def listar_paises(paises):
    mostrar_titulo("Listado de paises")

    if lista_vacia(paises):
        return

    print(f"{'Pais':<25} {'Poblacion':>15} {'Superficie (km2)':>20}   {'Continente':<15}")
    print("-" * 80)
    for pais in paises:
        print(
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>15,} "
            f"{pais['superficie']:>20,}   "
            f"{pais['continente']:<15}"
        )
    print(f"\nTotal: {len(paises)} pais/es.")


def agregar_pais(paises):
    mostrar_titulo("Agregar pais")

    resultado = pedir_nombre("Nombre del pais: ", max_intentos=3)
    if resultado is None:
        return True
    nombre = formatear_texto(resultado).title()

    if buscar_por_nombre_exacto(nombre, paises) is not None:
        print(f"Ya existe un pais en la base de datos con el nombre '{nombre}'.")
        return

    poblacion = pedir_entero_positivo("Poblacion: ", max_intentos=3)
    if poblacion is None:
        return True

    superficie = pedir_entero_positivo("Superficie (km2): ", max_intentos=3)
    if superficie is None:
        return True

    continente = pedir_continente("Continente: ")
    if continente is None:
        return True

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(pais)
    guardar_paises(paises)
    mostrar_exito(f"Pais '{nombre}' agregado correctamente.")


def modificar_pais(paises):
    mostrar_titulo("Modificar pais")

    if lista_vacia(paises):
        return

    nombre = pedir_nombre("Nombre del pais a modificar: ", max_intentos=3)
    if nombre is None:
        return True
    pais = buscar_por_nombre_exacto(nombre, paises)
    if pais is None:
        print(f"No se encontro el pais '{nombre}'.")
        return

    print(f"\n{'Nombre':<25} {'Poblacion':>15} {'Superficie (km2)':>20}   {'Continente':<15}")
    print("-" * 80)
    print(f"{pais['nombre']:<25} {pais['poblacion']:>15,} {pais['superficie']:>20,}   {pais['continente']:<15}")
    print()

    nueva_poblacion = pedir_entero_positivo("Nueva poblacion (dejar vacío para no modificar): ", opcional=True)
    nueva_superficie = pedir_entero_positivo("Nueva superficie (dejar vacío para no modificar): ", opcional=True)
    nuevo_continente = pedir_continente("Nuevo continente (dejar vacío para no modificar): ", opcional=True)

    if nueva_poblacion is None and nueva_superficie is None and nuevo_continente is None:
        print("No se realizaron cambios.")
        return

    if nueva_poblacion is not None:
        pais["poblacion"] = nueva_poblacion
    if nueva_superficie is not None:
        pais["superficie"] = nueva_superficie
    if nuevo_continente is not None:
        pais["continente"] = nuevo_continente

    guardar_paises(paises)
    mostrar_exito(f"Pais '{pais['nombre']}' modificado correctamente.")


def eliminar_pais(paises):
    mostrar_titulo("Eliminar pais")

    if lista_vacia(paises):
        return

    nombre = pedir_nombre("Nombre del pais a eliminar: ", max_intentos=3)
    if nombre is None:
        return True

    pais = buscar_por_nombre_exacto(nombre, paises)
    if pais is None:
        print(f"No se encontro el pais '{nombre}'.")
        return

    if questionary.select(f"Confirma eliminar '{pais['nombre']}'?", choices=["No", "Si"]).ask() == "Si":
        paises.remove(pais)
        guardar_paises(paises)
        mostrar_exito(f"Pais '{pais['nombre']}' eliminado correctamente.")
    else:
        print("Operacion cancelada.")


def buscar_pais(paises):
    mostrar_titulo("Buscar pais")

    if lista_vacia(paises):
        return

    termino = pedir_nombre("Nombre a buscar: ", max_intentos=3)
    if termino is None:
        return True

    termino_norm = formatear_texto(termino.lower())
    resultados = [p for p in paises if termino_norm in formatear_texto(p["nombre"].lower())]

    if not resultados:
        print(f"No se encontraron paises con '{termino}'.")
        return

    print(f"\n{'Nombre':<25} {'Poblacion':>15}   {'Superficie (km2)':>18}   {'Continente':<15}")
    print("-" * 80)
    for pais in resultados:
        print(
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>15,} "
            f"{pais['superficie']:>20,}   "
            f"{pais['continente']:<15}"
        )
    print(f"\n{len(resultados)} resultado/s.")
