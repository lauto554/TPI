import os
import unicodedata
import questionary

CONTINENTES_VALIDOS = ["Africa", "America", "Asia", "Europa", "Oceania", "Antartida"]

def lista_vacia(paises):
    if not paises:
        print("No hay paises cargados.")
        return True
    return False

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresione Enter para continuar...")

def formatear_texto(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("ascii")

def mostrar_titulo(titulo):
    print("=" * 50)
    print(titulo)
    print("=" * 50)

def mostrar_exito(mensaje):
    linea = "═" * (len(mensaje) + 4)
    print(f"\n╔{linea}╗")
    print(f"║  {mensaje}  ║")
    print(f"╚{linea}╝\n")

def pedir_int(mensaje):
    while True:
        try:
            dato = input(mensaje.strip())
            if not dato:
                raise ValueError("El campo no puede estar vacio")
            if int(dato) < 0:
                raise ValueError("Debe ser mayor que 0")
            return int(dato)
        except ValueError as e:
            print(f"\nERROR: {e}")

def pedir_entero_positivo(mensaje, opcional=False, max_intentos=None):
    intentos = 0

    while True:
        dato = input(mensaje).strip()

        if not dato:
            if opcional:
                return None
            print("El campo no puede estar vacio.")
        elif not dato.isdigit() or int(dato) <= 0:
            print("Debe ingresar un numero entero mayor a 0.")
        else:
            return int(dato)

        if max_intentos is not None:
            intentos += 1
            
            if intentos >= max_intentos:
                if questionary.select("Demasiados intentos. Desea volver al menu?", choices=["Si", "No"]).ask() == "Si":
                    return None
                intentos = 0

def pedir_nombre(mensaje, max_intentos=None):
    intentos = 0

    while True:
        valor = input(mensaje).strip()

        if not valor:
            print("El campo no puede estar vacio.")
        elif any(c.isdigit() for c in valor):
            print("El nombre no puede contener numeros.")
        else:
            return valor

        if max_intentos is not None:
            intentos += 1

            if intentos >= max_intentos:
                if questionary.select("Demasiados intentos. Desea volver al menu?", choices=["Si", "No"]).ask() == "Si":
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

    seleccion = questionary.select(mensaje, choices=choices).ask()

    if seleccion == "(No modificar)":
        return None
    return seleccion


def pedir_texto(mensaje):
    while True:
        try: 
            texto = input(mensaje).strip()
            if not texto:
                raise ValueError("El campo no puede estar vacio")
            return texto
        except ValueError as e:
            print(f"\nERROR: {e}")


def pedir_rango(mensaje_min, mensaje_max):
    while True:
        try:
            minimo = pedir_int(mensaje_min)
            maximo = pedir_int(mensaje_max)
            if minimo > maximo:
                raise ValueError("El minimo no puede ser superior al maximo")
            return minimo, maximo
        except ValueError as e:
            print(f"\nERROR: {e}")


def mostrar_resultados(resultados):
    if not resultados:
        print("\nNo se encontraron paises")
        return
    print()
    for pais in resultados:
        print(
            f"{pais['nombre']} | "
            f"{pais['continente']} | "
            f"{pais['poblacion']} habitantes | "
            f"{pais['superficie']} km²"
        )