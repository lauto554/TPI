# TPI - Programacion I

Esqueleto inicial del Trabajo Practico Integrador.

## Objetivo

Base funcional para trabajar en grupo de forma asincronica, separando responsabilidades por archivo sin resolver todavia la consigna completa.

## Estructura

```text
main.py              # Punto de entrada
menu.py              # Menu principal con questionary
datos.py             # Carga, guardado y ABM de paises
filtros.py           # Busquedas y filtros
ordenamientos.py     # Ordenamientos
estadisticas.py      # Calculos y reportes
utils.py             # Limpieza de consola, pausa y helpers comunes
requirements.txt     # Dependencias
```

## Formato acordado para un pais

```python
pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

Todas las funciones deben recibir y devolver datos respetando ese formato.

## Instalacion

```bash
pip install -r requirements.txt
```

## Ejecucion

```bash
python main.py
```

## Flujo sugerido

- Crear una rama por modulo o tarea.
- No trabajar los dos sobre el mismo archivo al mismo tiempo si no es necesario.
- Abrir pull request antes de mezclar cambios a `main`.
- Mantener `main.py` limpio: solo debe iniciar el programa.

