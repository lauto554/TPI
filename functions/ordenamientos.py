import questionary

from functions.utils import mostrar_resultados, limpiar_consola, pausar, lista_vacia
from functions.estilos import mostrar_titulo, ESTILO_MENU

def ordenar_por_nombre(paises, descendente=False):
    return sorted(
        paises,
        key=lambda pais: pais["nombre"].lower(),
        reverse=descendente
    )


def ordenar_por_poblacion(paises, descendente=False):
    return sorted(
        paises,
        key=lambda pais: pais["poblacion"],
        reverse=descendente
    )


def ordenar_por_superficie(paises, descendente=False):
    return sorted(
        paises,
        key=lambda pais: pais["superficie"],
        reverse=descendente
    )


def elegir_orden():
    opcion = questionary.select(
        "Orden:",
        choices=[
            "⬆️​  Ascendente",
            "⬇️​  Descendente"
        ], style= ESTILO_MENU
    ).ask()
    return "Descendente" in opcion


def ordenar_paises(paises):
    mostrar_titulo("Ordenar Paises")
    
    if not paises:
        lista_vacia(paises)
        return
    while True:
        limpiar_consola()
        opcion = questionary.select(
            "Seleccione un ordenamiento:",
            choices = [
                "🔤 Por nombre",
                "👥 Por población",
                "📐 Por superficie",
                "🔙 Volver"
            ], style= ESTILO_MENU
        ).ask()
        if opcion == "🔙 Volver":
            return True
        descendente = elegir_orden()
        if opcion == "🔤 Por nombre":
            resultados = ordenar_por_nombre(paises, descendente)
        elif opcion == "👥 Por población":
            resultados = ordenar_por_poblacion(paises, descendente)
        elif opcion == "📐 Por superficie":
            resultados = ordenar_por_superficie(paises, descendente)
        mostrar_resultados(resultados)
        pausar()