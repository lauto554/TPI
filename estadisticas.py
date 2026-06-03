try:
    import questionary
except ImportError:
    questionary = None


from utils import limpiar_consola, pausar, mostrar_titulo

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
    while True:
        limpiar_consola()
        mostrar_titulo("Estadisticas")
        opcion = questionary.select(
            "Seleccione una estadistica:",
            choices = [
                "Pais con mayor población",
                "Pais con menor población",
                "Promedio de población",
                "Promedio de superficie",
                "Cantidad de paises por continente",
                "Volver"
            ]
        ).ask()
        if opcion == "Volver":
            break
        elif opcion == "Pais con mayor población":
            pais = mayor_poblacion(paises)
            print(f"\nPais: {pais['nombre']}")
            print(f"Poblacion: {pais['poblacion']}")
        elif opcion == "Pais con menor población":
            pais = menor_poblacion(paises)
            print(f"\nPais: {pais['nombre']}")
            print(f"Poblacion: {pais['poblacion']}")
        elif opcion == "Promedio de población":
            promedio = calcular_promedio_poblacion(paises)
            print(f"\nPromedio de población: {promedio:.2f}")
        elif opcion == "Promedio de superficie":
            promedio = calcular_promedio_superficie(paises)
            print(f"\nPromedio de superficie: {promedio:.2f}")
        elif opcion == "Cantidad de paises por continente":
            cantidades = contar_por_continente(paises)
            for continente, cantidad in cantidades.items():
                print(f"{continente}: {cantidad}")
        pausar()