import os
import unicodedata
import questionary
from rich.console import Console
from functions.estilos import ESTILO_MENU, mostrar_tabla_paises

console = Console()

CONTINENTES_VALIDOS = ["Africa", "America", "Asia", "Europa", "Oceania", "Antartida"]

def lista_vacia(paises):
    if not paises:
        console.print("[bold red]No hay paises cargados.[bold red]")
        return True
    return False

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione Enter para continuar...")

def formatear_texto(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("ascii")

def pedir_entero_positivo(mensaje, opcional=False, max_intentos=None):
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

        if max_intentos is not None:
            intentos += 1
            
            if intentos >= max_intentos:
                if questionary.select("Demasiados intentos. Desea volver al menu?", choices=["✅ Si", "❌​ No"], style= ESTILO_MENU).ask() == "✅ Si":
                    return None
                intentos = 0

def pedir_nombre(mensaje, max_intentos=None):
    intentos = 0

    while True:
        valor = input(mensaje).strip()

        if not valor:
            console.print("[bold red]El campo no puede estar vacio.[bold red]")
        elif any(c.isdigit() for c in valor):
            console.print("[bold red]El nombre no puede contener numeros.[bold red]")
        else:
            return valor

        if max_intentos is not None:
            intentos += 1

            if intentos >= max_intentos:
                if questionary.select("Demasiados intentos. Desea volver al menu?", choices=["✅ Si", "❌​ No"], style= ESTILO_MENU).ask() == "✅ Si":
                    return None
                intentos = 0

def buscar_por_nombre_exacto(nombre, paises):
    nombre_formateado = formatear_texto(nombre.lower())

    for pais in paises:
        if formatear_texto(pais["nombre"].lower()) == nombre_formateado:
            return pais
    return None

def pedir_continente(mensaje, opcional=False):
    choices = CONTINENTES_VALIDOS.copy()  # copia para no modificar la lista original
    if opcional:
        choices.insert(0, "(No modificar)") # lo inserto al principio para que sea la primera opcion

    seleccion = questionary.select(mensaje, choices=choices, style= ESTILO_MENU).ask()

    if seleccion == "(No modificar)":
        return None
    return seleccion

def pedir_rango(mensaje_min, mensaje_max):
    while True:
        try:
            minimo = pedir_entero_positivo(mensaje_min, opcional= False, max_intentos= 3)
            if minimo is None:
                return None
            maximo = pedir_entero_positivo(mensaje_max, opcional= False, max_intentos= 3)
            if maximo is None:
                return None
            if minimo > maximo:
                raise ValueError("El minimo no puede ser superior al maximo")
            return minimo, maximo
        except ValueError as e:
            console.print(f"[bold red]\nERROR: {e}[bold red]")


def mostrar_resultados(resultados):
    if not resultados:
        print("\nNo se encontraron paises")
        return
    print()
    mostrar_tabla_paises(resultados)