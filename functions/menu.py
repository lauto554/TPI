import questionary

from functions.datos import agregar_pais, buscar_pais, cargar_paises, eliminar_pais, guardar_paises, listar_paises, modificar_pais
from functions.estadisticas import mostrar_estadisticas
from functions.filtros import filtrar_paises
from functions.ordenamientos import ordenar_paises
from functions.utils import limpiar_consola, pausar
from functions.estilos import mostrar_titulo, ESTILO_MENU
from rich.console import Console

console = Console()

OPCIONES_MENU = {
    "🌎​ Listar paises": listar_paises,
    "➕ Agregar pais": agregar_pais,
    "✍️​  Modificar pais": modificar_pais,
    "❌​ Eliminar pais": eliminar_pais,
    "🔍​ Buscar pais": buscar_pais,
    "🌪️  Filtrar paises": filtrar_paises,
    "🔀 Ordenar paises": ordenar_paises,
    "📊 Estadisticas": mostrar_estadisticas,
}

OPCION_SALIR = "🚪 Salir"


def ejecutar_menu():
    paises = cargar_paises()

    while True:
        limpiar_consola()
        mostrar_titulo("TPI Programacion I - Paises")

        opcion = seleccionar_opcion()


        if opcion == OPCION_SALIR:
            guardar_paises(paises)
            console.print("\n[blue bold]PROGRAMA FINALIZADO.[blue bold]\n")
            break

        limpiar_consola()


        funcion = OPCIONES_MENU[opcion]
        ir_al_menu = funcion(paises)
        if ir_al_menu is not True:
            pausar()


def seleccionar_opcion():
    opciones = list(OPCIONES_MENU.keys()) + [OPCION_SALIR]
    return questionary.select("Seleccione una opcion:", choices=opciones, style= ESTILO_MENU).ask()