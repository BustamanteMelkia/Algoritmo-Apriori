# Algoritmo-Apriori
Algoritmo de Minería de datos que permite encontrar conjuntos de ítems frecuentes, los cuales sirven de base para generar reglas de asociación. 

**Reglas de Asociación.**
El objetivo de las reglas de asociación es encontrar
asociaciones o correlaciones entre los elementos u
objetos de bases de datos transaccionales, relacionales
o data warehouse.

**Conceptos**

- Soporte: El soporte del elemento o subconjunto X es el número de transacciones que contienen X dividido entre el total de transacciones.
- Umbral: soporte mínimo que debe cumplir un elemento o subconjunto para considerarse un conjunto frecuente.

**Datos de entrada:**

Los datos requeridos para la ejecución del programa son obtenidos desde un archivo de texto. Dicho archivo debe ubicarse en la carpeta raíz del programa.
El formato de los datos almacenados en el archivo se describe a continuación:

- El valor del umbral se especifica en la primera línea del archivo y corresponde a un tipo de dato decimal.
- A partir de la segunda línea de archivo, cada línea de datos corresponde a una transacción Una transacción está conformada por una sucesión de elementos separados por una coma. Un elemento es identificado mediante un número entero mayor a cero.

**Datos de Salida**
Los datos mostrados en pantalla corresponden a los conjuntos frecuentes, que representan las combinaciones que superan el umbral especificado en el archivo de entrada.
El número de conjuntos de salida cambia, incluso para las mismas transacciones de entrada si el umbral es diferente.

Los conjuntos son listas mostradas según su orden, es decir:


Elementos individuales
Combinaciones pares
Combinaciones a tercias
...
Combinaciones N

**Ejecución del programa**

`py main.py`

