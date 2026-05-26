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

