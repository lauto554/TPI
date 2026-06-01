import os


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione Enter para continuar...")


def mostrar_titulo(titulo):
    print("=" * 50)
    print(titulo)
    print("=" * 50)


def mostrar_funcion_pendiente(nombre_funcion):
    print(f"La funcion '{nombre_funcion}' esta pendiente de implementacion.")


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