try:
    import questionary
except ImportError:
    questionary = None

from functions.datos import agregar_pais, buscar_pais, cargar_paises, eliminar_pais, guardar_paises, listar_paises, modificar_pais
from functions.estadisticas import mostrar_estadisticas
from functions.filtros import filtrar_paises
from functions.ordenamientos import ordenar_paises
from functions.utils import limpiar_consola, mostrar_titulo, pausar


OPCIONES_MENU = {
    "Listar paises": listar_paises,
    "Agregar pais": agregar_pais,
    "Modificar pais": modificar_pais,
    "Eliminar pais": eliminar_pais,
    "Buscar pais": buscar_pais,
    "Filtrar paises": filtrar_paises,
    "Ordenar paises": ordenar_paises,
    "Estadisticas": mostrar_estadisticas,
}

OPCION_SALIR = "Salir"


def ejecutar_menu():
    if questionary is None:
        print("Falta instalar questionary. Ejecute: pip install -r requirements.txt")
        pausar()
        return

    paises = cargar_paises()

    while True:
        limpiar_consola()
        mostrar_titulo("TPI Programacion I - Paises")

        opcion = seleccionar_opcion()

        limpiar_consola()

        if opcion == OPCION_SALIR:
            guardar_paises(paises)
            print("Programa finalizado.")
            break

        funcion = OPCIONES_MENU[opcion]
        ir_al_menu = funcion(paises)
        if ir_al_menu is not True:
            pausar()


def seleccionar_opcion():
    opciones = list(OPCIONES_MENU.keys()) + [OPCION_SALIR]

    return questionary.select("Seleccione una opcion:", choices=opciones).ask()
