from utils import mostrar_funcion_pendiente, mostrar_titulo
import csv


RUTA_ARCHIVO = "paises.csv"
CAMPOS_PAIS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises():
    paises = []
    try:
        with open(
            "paises.csv",
            mode="r",
            encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("Error: no se encontró el archivo paises.csv")
    except KeyError:
        print("Error: el formato del CSV es incorrecto")
    except ValueError:
        print("Error: hay datos numéricos inválidos en el CSV")
    return paises


def guardar_paises(paises):
    mostrar_funcion_pendiente("guardar_paises")


def listar_paises(paises):
    mostrar_titulo("Listado de paises")

    if not paises:
        print("No hay paises cargados.")
        return

    for pais in paises:
        print(pais)


def agregar_pais(paises):
    mostrar_funcion_pendiente("agregar_pais")


def modificar_pais(paises):
    mostrar_funcion_pendiente("modificar_pais")


def eliminar_pais(paises):
    mostrar_funcion_pendiente("eliminar_pais")

