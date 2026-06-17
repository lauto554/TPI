import questionary
from functions.utils import limpiar_consola, pausar, lista_vacia
from functions.estilos import mostrar_titulo, ESTILO_MENU, mostrar_tabla_paises, mostrar_tabla_continentes, mostrar_resultado_promedio, formatear_numero

def mayor_poblacion(paises):
    return max(
        paises,
        key= lambda pais: pais['poblacion']
    )

def menor_poblacion(paises):
    return min(
        paises,
        key= lambda pais: pais['poblacion']
    )


def calcular_promedio_poblacion(paises):
    total = 0
    for pais in paises:
        total += pais['poblacion']
    return total / len(paises)


def calcular_promedio_superficie(paises):
    total = 0
    for pais in paises:
        total += pais['superficie']
    return total / len(paises)


def contar_por_continente(paises):
    cantidades = {}
    for pais in paises:
        continente = pais['continente']
        if continente in cantidades:
            cantidades[continente] += 1
        else:
            cantidades[continente] = 1
    return cantidades


def mostrar_estadisticas(paises):
    mostrar_titulo("Estadisticas")
    
    if not paises:
        lista_vacia(paises)
        return
    while True:
        opcion = questionary.select(
            "Seleccione una estadistica:",
            choices = [
                "📈 Pais con mayor población",
                "📉 Pais con menor población",
                "👥 Promedio de población",
                "📐 Promedio de superficie",
                "🗺️  Cantidad de paises por continente",
                "🔙 Volver"
            ], style= ESTILO_MENU
        ).ask()
        if opcion == "🔙 Volver":
            return True
        elif opcion == "📈 Pais con mayor población":
            pais = mayor_poblacion(paises)
            mostrar_tabla_paises([pais])
        elif opcion == "📉 Pais con menor población":
            pais = menor_poblacion(paises)
            mostrar_tabla_paises([pais])
        elif opcion == "👥 Promedio de población":
            promedio = calcular_promedio_poblacion(paises)
            mostrar_resultado_promedio(
                "Cantidad promedio de habitantes entre todos los países cargados.",
                formatear_numero(promedio, 2),
                "habitantes",
            )
        elif opcion == "📐 Promedio de superficie":
            promedio = calcular_promedio_superficie(paises)
            mostrar_resultado_promedio(
                "Extensión territorial promedio entre todos los países cargados.",
                formatear_numero(promedio, 2),
                "km²",
            )
        elif "Cantidad de paises por continente" in opcion:
            mostrar_tabla_continentes(contar_por_continente(paises))
        pausar()