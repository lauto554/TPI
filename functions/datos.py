import csv
import unicodedata
import questionary
from functions.utils import lista_vacia, formatear_texto, buscar_por_nombre_exacto, pedir_nombre, pedir_continente, pedir_entero_positivo
from functions.estilos import mostrar_titulo, ESTILO_MENU, mostrar_tabla_paises
from rich.console import Console

console = Console()

RUTA_ARCHIVO = "paises.csv"
CAMPOS_PAIS = ["nombre", "poblacion", "superficie", "continente"]


######################### CSV #########################
def cargar_paises():
    paises = []
    try:
        with open(RUTA_ARCHIVO, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip(),
                }
                paises.append(pais)
    except FileNotFoundError:
        console.print("[yellow bold]Archivo CSV no encontrado. Se inicia con lista vacia.[yellow bold]")
    except (KeyError, ValueError) as e:
        console.print(f"[red bold]Error al leer el CSV: {e}[red bold]")
    return paises


def guardar_paises(paises):
    try:
        with open(RUTA_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PAIS)
            escritor.writeheader()
            for pais in paises:
                fila = {
                    "nombre": formatear_texto(pais["nombre"]).title(),
                    "poblacion": pais["poblacion"],
                    "superficie": pais["superficie"],
                    "continente": formatear_texto(pais["continente"]).title(),
                }
                escritor.writerow(fila)
    except IOError as e:
        console.print(f"[red bold]Error al guardar el archivo: {e}[red bold]")


########################## ABM #########################
def listar_paises(paises):
    mostrar_titulo("Listado de paises")
    if lista_vacia(paises):
        return
    mostrar_tabla_paises(paises)


def agregar_pais(paises):
    mostrar_titulo("Agregar pais")

    resultado = pedir_nombre("Nombre del pais: ", max_intentos=3)
    if resultado is None:
        return True
    nombre = formatear_texto(resultado).title()

    if buscar_por_nombre_exacto(nombre, paises) is not None:
        console.print(f"[yellow bold]Ya existe un pais en la base de datos con el nombre '{nombre}'.[yellow bold]")
        return

    poblacion = pedir_entero_positivo("Poblacion: ", max_intentos=3)
    if poblacion is None:
        return True

    superficie = pedir_entero_positivo("Superficie (km2): ", max_intentos=3)
    if superficie is None:
        return True

    continente = pedir_continente("Continente: ")
    if continente is None:
        return True

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(pais)
    guardar_paises(paises)
    mostrar_titulo(f"Pais '{nombre}' agregado correctamente.")


def modificar_pais(paises):
    mostrar_titulo("Modificar pais")

    if lista_vacia(paises):
        return

    nombre = pedir_nombre("Nombre del pais a modificar: ", max_intentos=3)
    if nombre is None:
        return True
    pais = buscar_por_nombre_exacto(nombre, paises)
    if pais is None:
        console.print(f"[yellow bold]No se encontro el pais '{nombre}'.[yellow bold]")
        return

    mostrar_tabla_paises([pais])
    print()

    nueva_poblacion = pedir_entero_positivo("Nueva poblacion (dejar vacío para no modificar): ", opcional=True)
    nueva_superficie = pedir_entero_positivo("Nueva superficie (dejar vacío para no modificar): ", opcional=True)
    nuevo_continente = pedir_continente("Nuevo continente (dejar vacío para no modificar): ", opcional=True)

    if nueva_poblacion is None and nueva_superficie is None and nuevo_continente is None:
        console.print("[yellow bold]No se realizaron cambios.[yellow bold]")
        return

    if nueva_poblacion is not None:
        pais["poblacion"] = nueva_poblacion
    if nueva_superficie is not None:
        pais["superficie"] = nueva_superficie
    if nuevo_continente is not None:
        pais["continente"] = nuevo_continente

    guardar_paises(paises)
    mostrar_titulo(f"Pais '{pais['nombre']}' modificado correctamente.")


def eliminar_pais(paises):
    mostrar_titulo("Eliminar pais")

    if lista_vacia(paises):
        return

    nombre = pedir_nombre("Nombre del pais a eliminar: ", max_intentos=3)
    if nombre is None:
        return True

    pais = buscar_por_nombre_exacto(nombre, paises)
    if pais is None:
        console.print(f"[yellow bold]No se encontro el pais '{nombre}'.[yellow bold]")
        return

    if questionary.select(f"Confirma eliminar '{pais['nombre']}'?", choices=["❌ No", "✅ Si"], style= ESTILO_MENU).ask() == "✅ Si":
        paises.remove(pais)
        guardar_paises(paises)
        mostrar_titulo(f"Pais '{pais['nombre']}' eliminado correctamente.")
    else:
        console.print("[green bold]Operacion cancelada.[green bold]")


def buscar_pais(paises):
    mostrar_titulo("Buscar pais")

    if lista_vacia(paises):
        return

    termino = pedir_nombre("Nombre a buscar: ", max_intentos=3)
    if termino is None:
        return True

    termino_norm = formatear_texto(termino.lower())
    resultados = [p for p in paises if termino_norm in formatear_texto(p["nombre"].lower())]

    if not resultados:
        console.print(f"[yellow bold]No se encontraron paises con '{termino}'.[yellow bold]")
        return
    print(f"\nResultados de la busqueda:")
    mostrar_tabla_paises(resultados)