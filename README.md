# Trabajo Practico Integrador - Programacion I

Repositorio correspondiente al Trabajo Practico Integrador de la materia Programacion I.

## Descripcion

El programa permite trabajar con informacion de paises mediante un menu por consola. La organizacion del proyecto se separa en distintos modulos para facilitar el desarrollo y la lectura del codigo.

## Requisitos

- Python 3
- Libreria `questionary`

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecucion

Desde la carpeta del proyecto:

```bash
python main.py
```

## Estructura del proyecto

```text
main.py              Punto de entrada del programa
menu.py              Menu principal
datos.py             Carga, guardado y gestion de paises
filtros.py           Funciones de busqueda y filtrado
ordenamientos.py     Funciones de ordenamiento
estadisticas.py      Calculos y estadisticas
utils.py             Funciones auxiliares
requirements.txt     Dependencias del proyecto
```

## Formato de datos

Cada pais se representa mediante un diccionario con la siguiente estructura:

```python
pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

La coleccion de paises se maneja como una lista de diccionarios.
