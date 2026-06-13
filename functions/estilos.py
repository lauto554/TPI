try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
    from rich import box
    rich_disponible = True
except ImportError:
    rich_disponible = False

try:
    import questionary
    ESTILO_MENU = questionary.Style([
        ("qmark",       "fg:#00bfff bold"),
        ("question",    "fg:#ffffff bold"),
        ("pointer",     "fg:#00bfff bold"),
        ("highlighted", "fg:#00bfff bold"),
        ("selected",    "fg:#aaffaa"),
        ("separator",   "fg:#555555"),
        ("instruction", "fg:#555555 italic"),
    ])
except ImportError:
    questionary = None
    ESTILO_MENU = None

console = Console() if rich_disponible else None

def mostrar_titulo(titulo: str,):
    if not rich_disponible:
        linea = "=" * 44
        print(linea)
        print(f"  {titulo}")
        print(linea)
        return
    contenido = Text(titulo, justify="center")
    contenido.stylize("bold white")
    console.print(
        Panel(
            contenido,
            style="bold blue",
            border_style="bright_blue",
            
            padding=(1, 4),
        )
    )
    console.print()

def mostrar_tabla_paises(paises: list):
    if not rich_disponible:
        print(f"{'Pais':<25} {'Poblacion':>15} {'Superficie (km2)':>20}   {'Continente':<15}")
        print("-" * 80)
        for pais in paises:
            print(
                f"{pais['nombre']:<25} "
                f"{pais['poblacion']:>15,} "
                f"{pais['superficie']:>20,}   "
                f"{pais['continente']:<15}"
            )
        print(f"\nTotal: {len(paises)} pais/es.")
        return
    tabla = Table(
        box=box.ROUNDED,
        border_style="bright_blue",
        header_style="bold white",
        show_lines= False,
        expand= False,
    )
    tabla.add_column("🌍  Pais",              style="bold cyan",         min_width=22, no_wrap=True)
    tabla.add_column("👥  Poblacion",         style="white",             min_width=15, justify="right")
    tabla.add_column("📐  Superficie (km²)",  style="white",             min_width=20, justify="right")
    tabla.add_column("🗺️   Continente",        style="bold bright_white", min_width=15, justify="right")
    for pais in paises:
        tabla.add_row(
            pais["nombre"],
            f"{pais['poblacion']:,}",
            f"{pais['superficie']:,}",
            pais["continente"],
        )
    console.print(tabla)
    console.print(f"\n[dim]Total: {len(paises)} pais/es.[/dim]")