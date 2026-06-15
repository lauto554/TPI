import questionary
from rich.console import Console
from functions.utils import limpiar_consola, pedir_rango, pausar, mostrar_resultados, pedir_continente, lista_vacia
from functions.estilos import mostrar_titulo, ESTILO_MENU

console = Console()

def filtrar_por_continente(paises, continente):
    resultado = []
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultado.append(pais)
    return resultado


def filtrar_por_poblacion(paises, poblacion_minima, poblacion_maxima):
    resultados = []
    for pais in paises:
        if poblacion_minima <= pais['poblacion'] <= poblacion_maxima:
            resultados.append(pais)
    return resultados


def filtrar_por_superficie(paises, superficie_minima, superficie_maxima):
    resultados = []
    for pais in paises:
        if superficie_minima <= pais['superficie'] <= superficie_maxima:
            resultados.append(pais)
    return resultados


def filtrar_paises(paises):
    if not paises:
        lista_vacia(paises)
        return
    while True:
        opcion = questionary.select(
            "Seleccione un filtro:",
            choices = [
                "🗺️  Por continente",
                "👥 Por población",
                "📐 Por superficie",
                "🔙 Volver"
            ], style= ESTILO_MENU
        ).ask()
        if opcion == "🔙 Volver":
            return True
        elif opcion == "🗺️  Por continente":
            continente = pedir_continente("Ingrese el continente: ")
            if continente is None:
                continue
            resultados = filtrar_por_continente(paises, continente)
            mostrar_resultados(
                resultados,
                mensaje_vacio=f"No se encontraron paises cargados para el continente '{continente}'.",
            )
        elif opcion == "👥 Por población":
            rango = pedir_rango("Población minima: ", "Población maxima: ")
            if rango is None:
                continue
            minimo, maximo = rango
            resultados = filtrar_por_poblacion(paises, minimo, maximo)
            mostrar_resultados(resultados, "Rango de población buscado", minimo, maximo, "habitantes")
        elif opcion == "📐 Por superficie":
            rango = pedir_rango("Superficie minima: ", "Superficie maxima: ")
            if rango is None:
                continue
            minimo, maximo = rango
            resultados = filtrar_por_superficie(paises, minimo, maximo)
            mostrar_resultados(resultados, "Rango de superficie buscado", minimo, maximo, "km²")
        pausar()
        limpiar_consola()