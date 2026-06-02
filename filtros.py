try:
    import questionary
except ImportError:
    questionary = None

from utils import mostrar_funcion_pendiente, mostrar_titulo, limpiar_consola, pedir_rango, pedir_texto, pausar, mostrar_resultados


def filtrar_paises(paises):
    while True:
        limpiar_consola()
        mostrar_titulo("Filtrar Paises")
        opcion = questionary.select(
            "Seleccione un filtro:",
            choices = [
                "Por continente",
                "Por población",
                "Por superficie",
                "Volver"
            ]
        ).ask()
        if opcion == "Volver":
            break
        elif opcion == "Por continente":
            continente = pedir_texto("Ingrese el continente: ")
            resultados = filtrar_por_continente(paises, continente)
            mostrar_resultados(resultados)
        elif opcion == "Por población":
            minimo, maximo = pedir_rango("Población minima: ", "Población maxima: ")
            resultados = filtrar_por_poblacion(paises, minimo, maximo)
            mostrar_resultados(resultados)
        elif opcion == "Por superficie":
            minimo, maximo = pedir_rango("Superficie minima: ", "Superficie maxima: ")
            resultados = filtrar_por_superficie(paises, minimo, maximo)
            mostrar_resultados(resultados)
        pausar()


def buscar_paises(paises):
    mostrar_funcion_pendiente("buscar_paises")


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

