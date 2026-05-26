from utils import mostrar_funcion_pendiente, mostrar_titulo


RUTA_ARCHIVO = "paises.csv"
CAMPOS_PAIS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises():
    mostrar_funcion_pendiente("cargar_paises")
    return []


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

