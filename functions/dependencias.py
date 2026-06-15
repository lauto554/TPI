# Codigos ANSI para colorear la consola sin usar librerias (puedne no estar instaladas).
AMARILLO = "\033[33m"
CYAN = "\033[96m"
RESET = "\033[0m"   # vuelve al color por defecto
NEGRITA = "\033[1m"

def verificar_dependencias():
    """Comprueba questionary y rich antes de iniciar el programa."""
    faltantes = []
    try:
        import questionary
    except ImportError:
        faltantes.append("questionary")
    try:
        import rich
    except ImportError:
        faltantes.append("rich")
    if not faltantes:
        return True
    print(f"\n{AMARILLO}{NEGRITA}Faltan dependencias: {', '.join(faltantes)}{RESET}")
    print(f"{CYAN}Ejecute: pip install -r requirements.txt{RESET}")
    input(f"\n{NEGRITA}Presione Enter para continuar...{RESET}")
    return False
