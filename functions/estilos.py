from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box
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

console = Console()

def mostrar_titulo(titulo: str,):
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

def formatear_numero(numero, decimales=None):
    if decimales is None:
        return f"{numero:,}".replace(",", ".")
    texto = f"{numero:,.{decimales}f}"
    entero, decimal = texto.rsplit(".", 1)
    return f"{entero.replace(',', '.')},{decimal}"

def mostrar_tabla_paises(paises: list):
    tabla = Table(
        box=box.ROUNDED,
        border_style="bright_blue",
        header_style="bold white",
        show_lines=False,
        expand=False,
    )
    tabla.add_column("🌍  Pais",              style="bold cyan",         min_width=22, no_wrap=True)
    tabla.add_column("👥  Poblacion",         style="white",             min_width=15, justify="right")
    tabla.add_column("📐  Superficie (km²)",  style="white",             min_width=20, justify="right")
    tabla.add_column("🗺️   Continente",        style="bold bright_white", min_width=15, justify="right")
    for pais in paises:
        tabla.add_row(
            pais["nombre"],
            formatear_numero(pais['poblacion']),
            formatear_numero(pais['superficie']),
            pais["continente"],
        )
    console.print(tabla)
    console.print(f"\n[dim]Total: {len(paises)} pais/es.[/dim]")

def mostrar_tabla_continentes(cantidades: dict):
    tabla = Table(
        box=box.ROUNDED,
        border_style="bright_blue",
        header_style="bold white",
        show_lines=False,
        expand=False,
    )
    tabla.add_column("🗺️  Continente", style="bold cyan", min_width=22, no_wrap=True)
    tabla.add_column("📊  Total", style="white", min_width=10, justify="right")
    for continente in sorted(cantidades):
        tabla.add_row(continente, formatear_numero(cantidades[continente]))
    console.print(tabla)
    console.print(f"\n[dim]Total: {formatear_numero(sum(cantidades.values()))} pais/es.[/dim]")

def mostrar_resultado_promedio(descripcion, valor, unidad):
    console.print(f"\n[dim]{descripcion}[/dim]")
    console.print(f"[bold bright_blue]{valor}[/bold bright_blue] [bright_blue]{unidad}[/bright_blue]")

def mostrar_rango_busqueda(etiqueta, minimo, maximo, unidad=""):
    unidad_texto = f" {unidad}" if unidad else ""
    console.print(
        f"\n[dim]{etiqueta}:[/dim] "
        f"[bold bright_blue]{formatear_numero(minimo)}[/bold bright_blue] "
        f"[dim]-[/dim] "
        f"[bold bright_blue]{formatear_numero(maximo)}[/bold bright_blue]"
        f"[bright_blue]{unidad_texto}[/bright_blue]"
    )
