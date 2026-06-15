import os
import unicodedata
import questionary
from rich.console import Console
from functions.estilos import ESTILO_MENU, mostrar_tabla_paises, mostrar_rango_busqueda

console = Console()

CONTINENTES_VALIDOS = ["Africa", "America", "Asia", "Europa", "Oceania", "Antartida"]

def lista_vacia(lista):
    if not lista:
        console.print("[yellow bold]No hay datos de países cargados para esta operacion.[yellow bold]")
        console.print("Por favor, cargue paises en la seccion de 'Agregar pais'")
        return True
    return False

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione Enter para continuar...")

def formatear_texto(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("ascii")

def manejar_max_intentos(intentos, max_intentos=3):
    intentos += 1
    if intentos < max_intentos:
        return intentos, False
    if questionary.select(
        "Demasiados intentos. Desea volver al menu?",
        choices=["✅ Si", "❌​ No"],
        style=ESTILO_MENU,
    ).ask() == "✅ Si":
        return 0, True
    return 0, False

def pedir_entero_positivo(mensaje, opcional=False):
    intentos = 0

    while True:
        dato = input(mensaje).strip()

        if not dato:
            if opcional:
                return None
            console.print("[bold red]El campo no puede estar vacio.[bold red]")
        elif not dato.isdigit() or int(dato) <= 0:
            console.print("[bold red]Debe ingresar un numero entero mayor a 0.[bold red]")
        else:
            return int(dato)

        intentos, volver = manejar_max_intentos(intentos)
        if volver:
            return None

def pedir_nombre(mensaje):
    intentos = 0

    while True:
        valor = input(mensaje).strip()

        if not valor:
            console.print("[bold red]El campo no puede estar vacio.[bold red]")
        elif any(c.isdigit() for c in valor):
            console.print("[bold red]El nombre no puede contener numeros.[bold red]")
        else:
            return valor

        intentos, volver = manejar_max_intentos(intentos)
        if volver:
            return None

def buscar_por_nombre_exacto(nombre, paises):
    nombre_formateado = formatear_texto(nombre.lower())

    for pais in paises:
        if formatear_texto(pais["nombre"].lower()) == nombre_formateado:
            return pais
    return None

def pedir_continente(mensaje, opcional=False):
    choices = CONTINENTES_VALIDOS.copy()  # copia para no modificar la lista original
    if opcional:
        choices.insert(0, "(No modificar)") # lo inserta al principio para que sea la primera opcion 

    seleccion = questionary.select(mensaje, choices=choices, style= ESTILO_MENU).ask()

    if seleccion == "(No modificar)":
        return None
    return seleccion

def pedir_rango(mensaje_min, mensaje_max):
    while True:
        try:
            minimo = pedir_entero_positivo(mensaje_min)
            if minimo is None:
                return None
            maximo = pedir_entero_positivo(mensaje_max)
            if maximo is None:
                return None
            if minimo > maximo:
                raise ValueError("El minimo no puede ser superior al maximo")
            return minimo, maximo
        except ValueError as e:
            console.print(f"[bold red]\nERROR: {e}[bold red]")

def mostrar_resultados(resultados, etiqueta_rango=None, minimo=None, maximo=None, unidad="", mensaje_vacio=None):
    if etiqueta_rango is not None:
        mostrar_rango_busqueda(etiqueta_rango, minimo, maximo, unidad)
    if not resultados:
        mensaje = mensaje_vacio or "No se encontraron paises."
        console.print(f"\n[yellow bold]{mensaje}[/yellow bold]")
        return
    console.print()
    mostrar_tabla_paises(resultados)