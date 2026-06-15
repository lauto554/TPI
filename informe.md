# Informe — Trabajo Práctico Integrador

> Borrador en Markdown. Al finalizar, exportar a **PDF** con hojas numeradas y formato profesional.

---

## Carátula

**Institución:** Universidad Tecnológica Nacional — Facultad Regional Mendoza  
**Carrera:** Tecnicatura Universitaria en Programación a Distancia  
**Materia:** Programación I  
**Proyecto:** Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas  

**Integrantes:**

| Nombre | Legajo | Correo |
|---|---|---|
| Lautaro Martinez | 54277 | lautaroj.martinez@alumnos.frm.utn.edu.ar |
| Luciano Pizarro | — | — |

**Fecha de entrega:** `[COMPLETAR]`

---

## Índice

1. Introducción
2. Marco teórico
   - 2.1 Listas
   - 2.2 Diccionarios
   - 2.3 Funciones
   - 2.4 Condicionales
   - 2.5 Ordenamientos
   - 2.6 Estadísticas básicas
   - 2.7 Archivos CSV
3. Decisiones técnicas y arquitectura
4. Dificultades y conclusiones
5. Bibliografía / webgrafía
6. Enlaces

*(Al pasar a PDF, completar con números de página reales.)*

---

## 1. Introducción

El presente Trabajo Práctico Integrador tiene como objetivo desarrollar una aplicación en Python capaz de gestionar información sobre países, aplicando los conceptos fundamentales de la materia Programación I: listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas básicas.

El sistema permite cargar datos desde un archivo CSV, consultarlos y generar indicadores a partir de un dataset de países. Cada registro contiene nombre, población, superficie y continente. El usuario interactúa con el programa mediante un menú en consola desde el cual puede listar, agregar, modificar, eliminar y buscar países, además de filtrarlos, ordenarlos y visualizar estadísticas.

La persistencia de los datos se realiza en el archivo `paises.csv`, que se lee al iniciar el programa y se actualiza al salir, de modo que los cambios realizados durante la ejecución queden guardados.

---

## 2. Marco teórico

> Cada apartado debe explicar el concepto **y cómo se aplicó en este proyecto**, con al menos una fuente bibliográfica.

### 2.1 Listas

Una **lista** en Python es una estructura de datos ordenada y mutable que permite almacenar una secuencia de elementos. Se utiliza cuando necesitamos guardar una colección de registros sobre los cuales vamos a iterar, filtrar u ordenar (Python Software Foundation, s.f.).

En este proyecto, la lista principal es `paises`, que contiene todos los países cargados desde el CSV. Cada operación del sistema trabaja sobre esa lista: al listar se recorre completa, al filtrar se construye una nueva lista con los resultados, y al agregar o eliminar un país se modifica directamente con `append()` o `remove()`.

### 2.2 Diccionarios

Un **diccionario** es una estructura clave-valor que permite representar entidades con distintos atributos. A diferencia de una lista indexada por posición, se accede a cada dato mediante una clave identificatoria (Python Software Foundation, s.f.).

Cada país del sistema se modela como un diccionario con cuatro claves: `nombre`, `poblacion`, `superficie` y `continente`. La colección completa es una lista de diccionarios, lo que combina la flexibilidad del diccionario para representar un registro con la lista para manejar el conjunto de países.

```python
pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
```

### 2.3 Funciones

Las **funciones** permiten dividir el programa en bloques reutilizables, cada uno con una responsabilidad definida. Esto mejora la legibilidad, facilita el mantenimiento y evita repetir código (Python Software Foundation, s.f.).

El proyecto está organizado en módulos dentro de la carpeta `functions/`. Por ejemplo, `datos.py` concentra la carga y guardado del CSV y las operaciones de ABM; `filtros.py`, `ordenamientos.py` y `estadisticas.py` encapsulan cada tipo de consulta; y `utils.py` reúne funciones auxiliares como validaciones de entrada y formateo de texto. El criterio aplicado fue **una función = una responsabilidad**.

### 2.4 Condicionales

Las **estructuras condicionales** (`if`, `elif`, `else`) permiten que el programa tome decisiones en función de condiciones booleanas. Son la base del menú, las validaciones de datos y el manejo de casos especiales (Python Software Foundation, s.f.).

En el sistema se utilizan condicionales para validar entradas del usuario (campos vacíos, números inválidos, país inexistente), para dirigir el flujo del menú según la opción elegida, y para mostrar mensajes distintos cuando una búsqueda o filtro no arroja resultados.

### 2.5 Ordenamientos

El **ordenamiento** consiste en reorganizar una secuencia de elementos según un criterio. En Python, la función `sorted()` devuelve una nueva lista ordenada y admite el parámetro `key` para definir por qué campo ordenar, y `reverse` para indicar orden ascendente o descendente (Python Software Foundation, s.f.).

El módulo `ordenamientos.py` implementa tres criterios: por nombre (alfabético), por población y por superficie. El usuario elige además si desea orden ascendente o descendente. Internamente se usa `sorted()` con una función lambda que indica el campo de comparación.

### 2.6 Estadísticas básicas

Las **estadísticas básicas** permiten obtener información resumida de un conjunto de datos numéricos. En este proyecto se aplican operaciones como máximo, mínimo, promedio y conteo por categoría (Python Software Foundation, s.f.).

El módulo `estadisticas.py` calcula: el país con mayor y menor población (`max()` y `min()`), el promedio de población y superficie (suma acumulada dividida la cantidad de países), y la cantidad de países por continente (recorrido con diccionario de conteo).

### 2.7 Archivos CSV

Un archivo **CSV** (Comma-Separated Values) almacena datos tabulares en texto plano, con campos separados por comas. Python incluye el módulo `csv` para leer y escribir este formato de manera sencilla (Python Software Foundation, s.f.).

El archivo `paises.csv` es la fuente de datos del sistema. Al iniciar, `cargar_paises()` utiliza `csv.DictReader` para leer cada fila como un diccionario. Al salir, `guardar_paises()` utiliza `csv.DictWriter` para persistir los cambios. Si el archivo no existe o contiene datos con formato incorrecto, el programa informa el error sin interrumpir la ejecución.

---

## 3. Decisiones técnicas y arquitectura

### 3.1 Estructura del proyecto

El proyecto sigue una arquitectura modular. El punto de entrada es `main.py`, que verifica las dependencias necesarias y ejecuta el menú principal.

La lógica del sistema se organiza en la carpeta `functions/`:

| Módulo | Responsabilidad |
|---|---|
| `menu.py` | Menú principal y enlace con cada funcionalidad |
| `datos.py` | Carga, guardado y gestión de países (ABM y búsqueda) |
| `filtros.py` | Filtrado por continente, población y superficie |
| `ordenamientos.py` | Ordenamiento por nombre, población y superficie |
| `estadisticas.py` | Cálculos estadísticos sobre el dataset |
| `utils.py` | Validaciones de entrada, formateo y funciones auxiliares |
| `estilos.py` | Tablas, títulos y formato visual en consola |
| `dependencias.py` | Verificación de librerías al iniciar el programa |

Los datos persisten en `paises.csv` en la raíz del proyecto. Las dependencias externas (`questionary` y `rich`) se declaran en `requirements.txt`.

### 3.2 Diagrama de flujo

`[COMPLETAR: insertar diagrama o imagen del flujo principal del menú.]`

```text
[Ejemplo de esquema — reemplazar o ampliar]

Inicio → Cargar CSV → Menú principal
  → Listar / Agregar / Modificar / Eliminar / Buscar
  → Filtrar / Ordenar / Estadísticas
  → Salir → Guardar CSV → Fin
```

### 3.3 Capturas de ejecución

`[COMPLETAR: referenciar capturas de consola — pueden reutilizarse las de assets/ del README.]`

- Menú principal: `assets/menu-principal.png`
- Listar países: `assets/listar-paises.png`
- Buscar país: `assets/buscar-pais.png`
- *(agregar filtro, ordenamiento, estadísticas cuando estén disponibles)*

### 3.4 Validaciones implementadas

El sistema incluye validaciones en distintos puntos para evitar errores y guiar al usuario:

- **Campos vacíos:** al agregar un país, no se permiten nombre, población, superficie ni continente vacíos.
- **Tipos de datos:** la población y la superficie deben ser enteros positivos; el nombre no puede contener números.
- **País duplicado:** al agregar, se verifica que no exista otro país con el mismo nombre.
- **País inexistente:** al modificar o eliminar, se informa si el nombre ingresado no está en la base de datos.
- **Máximo de intentos:** tras tres ingresos inválidos consecutivos, se ofrece volver al menú principal.
- **CSV inexistente o con formato incorrecto:** se muestra un mensaje de error y el programa continúa con lista vacía o datos parcialmente cargados.
- **Búsquedas y filtros sin resultados:** se informa claramente que no se encontraron países, indicando el criterio utilizado (término buscado, continente o rango).
- **Rango inválido:** al filtrar por población o superficie, el mínimo no puede ser mayor que el máximo.
- **Dependencias faltantes:** al iniciar, se verifica que `questionary` y `rich` estén instaladas antes de ejecutar el programa.

---

## 4. Dificultades y conclusiones

### 4.1 Dificultades encontradas

Una de las dificultades principales fue **visualizar los datos en consola de forma clara**. Cuando el programa mostraba tablas y resultados usando únicamente `print()`, la información resultaba difícil de leer: columnas desalineadas, mucho ruido visual y poca diferenciación entre títulos, datos y mensajes de error.

### 4.2 Cómo se resolvieron

Para mejorar la presentación en consola, buscamos una librería que nos ayudara a formatear la salida. Incorporamos **Rich**, que permite mostrar tablas alineadas, paneles de título, colores y estilos tipográficos. Centralizamos el formato visual en el módulo `estilos.py`, lo que permitió que listados, filtros, estadísticas y mensajes se muestren de manera ordenada y legible sin modificar la lógica de negocio de cada módulo.

### 4.3 Conclusiones y aprendizajes

Como conclusión del trabajo, aprendimos que una vez finalizado el MVP y las funcionalidades principales, resulta valioso pensar en el **usuario que va a utilizar el producto o servicio**. Mejorar la visualización y la experiencia de uso — incluso en una aplicación de consola — facilita la interacción y reduce errores. Separar la lógica del formato (datos vs. estilos) fue una decisión que nos permitió agregar esta capa de mejora sin reescribir el núcleo del programa.

---

## 5. Bibliografía / webgrafía

- Python Software Foundation. (s.f.). *Built-in Types — dict, list.* Documentación de Python 3. https://docs.python.org/3/library/stdtypes.html
- Python Software Foundation. (s.f.). *csv — CSV File Reading and Writing.* Documentación de Python 3. https://docs.python.org/3/library/csv.html
- Python Software Foundation. (s.f.). *Sorting HOW TO.* Documentación de Python 3. https://docs.python.org/3/howto/sorting.html
- Textualize. (s.f.). *Rich — Render rich text, tables, progress bars, syntax highlighting, markdown and more.* https://rich.readthedocs.io/
- `[Agregar fuentes de apuntes, libro de Programación I, etc.]`

---

## 6. Enlaces

| Recurso | Enlace |
|---|---|
| Repositorio GitHub | https://github.com/lauto554/TPI |
| Video demostración | `[PENDIENTE]` |
| README del proyecto | https://github.com/lauto554/TPI#readme |
