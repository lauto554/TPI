# Herramientas usadas en el TPI

Documentación de las librerías, módulos y técnicas de Python utilizadas en el proyecto.

---

## 1. `unicodedata` — Normalización de texto

**Módulo:** estándar de Python (`import unicodedata`)  
**Archivo:** `datos.py` → función `_formatear_texto`

### Qué hace

Elimina acentos y caracteres especiales de un texto, dejando solo letras ASCII básicas. Se usa para comparar y buscar nombres sin importar tildes.

### Código

```python
def _formatear_texto(texto):
    return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("ascii")
```

### Paso a paso

1. `normalize("NFD", texto)` — descompone letras con tilde: `"é"` → `"e"` + acento
2. `encode("ascii", "ignore")` — convierte a bytes ASCII y descarta lo que no cabe
3. `decode("ascii")` — vuelve a string

### Ejemplos

| Entrada   | Salida   |
|-----------|----------|
| `"México"` | `"Mexico"` |
| `"Perú"`   | `"Peru"`   |
| `"España"` | `"Espana"` |

### Dónde se usa

- Guardar países sin acentos (`guardar_paises`)
- Buscar sin distinguir tildes (`buscar_pais`, `_buscar_por_nombre_exacto`)
- Validar continentes ingresados por el usuario

---

## 2. `csv` — Lectura y escritura de archivos CSV

**Módulo:** estándar de Python (`import csv`)  
**Archivo:** `datos.py`  
**Datos:** `paises.csv`

### Qué hace

Lee y escribe datos tabulares (filas y columnas) en un archivo de texto separado por comas.

### Carga de datos

```python
with open(RUTA_ARCHIVO, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        pais = {
            "nombre": fila["nombre"].strip(),
            "poblacion": int(fila["poblacion"]),
            ...
        }
        paises.append(pais)
```

- `DictReader`: cada fila del CSV se convierte en un diccionario con las columnas como claves
- `encoding="utf-8"`: soporta caracteres especiales (tildes, ñ)
- `with open(...)`: cierra el archivo automáticamente al terminar

### Guardado de datos

```python
escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PAIS)
escritor.writeheader()
escritor.writerow(fila)
```

- `DictWriter`: escribe diccionarios como filas del CSV
- `writeheader()`: escribe la primera fila con los nombres de columnas

---

## 3. `questionary` — Menús interactivos en consola

**Librería externa** (instalar con `pip install questionary`)  
**Archivos:** `menu.py`, `datos.py`, `filtros.py`, `ordenamientos.py`, `estadisticas.py`

### Qué hace

Muestra menús con flechas ↑↓ para elegir opciones, en lugar de escribir números.

### Ejemplo

```python
opcion = questionary.select(
    "Seleccione una opcion:",
    choices=["Listar paises", "Agregar pais", "Salir"]
).ask()
```

### Import defensivo

```python
try:
    import questionary
except ImportError:
    questionary = None
```

Si no está instalada, el programa avisa en lugar de crashear.

---

## 4. `os` — Limpieza de consola multiplataforma

**Módulo:** estándar de Python (`import os`)  
**Archivo:** `utils.py`

### Qué hace

Limpia la pantalla de la terminal según el sistema operativo.

```python
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")
```

| Sistema   | Comando | `os.name` |
|-----------|---------|-----------|
| Windows   | `cls`   | `"nt"`    |
| Linux/Mac | `clear` | `"posix"` |

---

## 5. f-strings con formato — Tablas en consola

**Concepto de Python**  
**Archivo:** `datos.py` → `listar_paises`

### Qué hace

Alinea columnas en la salida por consola.

```python
print(f"{pais['nombre']:<25} {pais['poblacion']:>15,}")
```

| Formato | Significado | Ejemplo |
|---------|-------------|---------|
| `:<25`  | Alineado a la izquierda, 25 caracteres | `"Argentina          "` |
| `:>15`  | Alineado a la derecha, 15 caracteres | `"     45376763"` |
| `:,`    | Separador de miles | `45376763` → `45,376,763` |
| `:.2f`  | 2 decimales | `1234.567` → `1234.57` |

---

## 6. List comprehensions — Filtrado compacto

**Concepto de Python**  
**Archivo:** `datos.py` → `buscar_pais`

### Qué hace

Crea una lista filtrando elementos en una sola línea.

```python
resultados = [
    p for p in paises
    if termino_norm in _formatear_texto(p["nombre"].lower())
]
```

Equivale a:

```python
resultados = []
for p in paises:
    if termino_norm in _formatear_texto(p["nombre"].lower()):
        resultados.append(p)
```

---

## 7. `sorted()` con `lambda` — Ordenamiento

**Concepto de Python**  
**Archivo:** `ordenamientos.py`

### Qué hace

Ordena la lista de países según un criterio.

```python
sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
```

- `key=`: define por qué campo ordenar
- `lambda`: función anónima de una línea
- `reverse=True`: orden descendente (mayor a menor)

### Ejemplos

| Función | Ordena por |
|---------|------------|
| `ordenar_por_nombre` | `pais["nombre"].lower()` |
| `ordenar_por_poblacion` | `pais["poblacion"]` |
| `ordenar_por_superficie` | `pais["superficie"]` |
