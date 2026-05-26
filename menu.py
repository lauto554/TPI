try:
    import questionary
except ImportError:
    questionary = None

from datos import agregar_pais, cargar_paises, eliminar_pais, guardar_paises, listar_paises, modificar_pais
from estadisticas import mostrar_estadisticas
from filtros import buscar_paises, filtrar_paises
from ordenamientos import ordenar_paises
from utils import limpiar_consola, mostrar_titulo, pausar


def ejecutar_menu():
    paises = cargar_paises()

    while True:
        limpiar_consola()
        mostrar_titulo("TPI Programacion I - Paises")

        opcion = seleccionar_opcion()

        limpiar_consola()

        if opcion == "Listar paises":
            listar_paises(paises)
        elif opcion == "Agregar pais":
            agregar_pais(paises)
        elif opcion == "Modificar pais":
            modificar_pais(paises)
        elif opcion == "Eliminar pais":
            eliminar_pais(paises)
        elif opcion == "Buscar paises":
            buscar_paises(paises)
        elif opcion == "Filtrar paises":
            filtrar_paises(paises)
        elif opcion == "Ordenar paises":
            ordenar_paises(paises)
        elif opcion == "Estadisticas":
            mostrar_estadisticas(paises)
        elif opcion == "Guardar cambios":
            guardar_paises(paises)
        elif opcion == "Salir":
            guardar_paises(paises)
            print("Programa finalizado.")
            break

        if opcion != "Salir":
            pausar()


def seleccionar_opcion():
    opciones = [
        "Listar paises",
        "Agregar pais",
        "Modificar pais",
        "Eliminar pais",
        "Buscar paises",
        "Filtrar paises",
        "Ordenar paises",
        "Estadisticas",
        "Guardar cambios",
        "Salir",
    ]

    if questionary is None:
        print("Falta instalar questionary. Ejecute: pip install -r requirements.txt")
        return "Salir"

    return questionary.select("Seleccione una opcion:", choices=opciones).ask()

