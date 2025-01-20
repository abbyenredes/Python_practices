# Creemos un generador de nombres para marcas
Hola autoestopista, bienvenido a este repaso que estoy realizando con python.
En este proyecto repasaremos como imprimir datos en la pantalla, así como el uso de strings.

## Usando Print
Con print podemos imprimir datos en la pantalla tales como strings:

```python

print("hello word")

```
> [!TIP]
>
> Para imprimir comillas dobles en una cadena de texto usaremos \\:
```python

print("hello \"word\" ")

```

Números enteros:
```python

print(50)

```
Números flotantes:
```python

print(3.14)

```

Operaciones aritméticas:
```python

print(50 + 30)

```

Boleanos:
```python

print(False)

```

Variables:
```python

name = "Bayta"
print(name)

```
> [!NOTE]
>
> Para compilar en python usamos: ``` python3 nomebre_archivo.py ```

## Usando input
Vamos a utilizar la función input para que el usuario final pueda introducir datos y nosotros podamos usarlos y almacenarlos:
```python

input("Dime tu nombre: ")

```
Con esto solo nos pedira nuestro dato, sin embargo no lo almacena ni muestra en ningun lado. Si queremos visualizarlo usaremos lo siguiente:

```python

print(input("dime tu nombre: "))

```
Si queremos hacerlo más personalizado:
```python

print("hola " + input("dime tu nombre: "))

```
¿Por qué el +? es para concatenar una cadena y así nuestro pequeño programa nos muestre un saludo personalizado.
Ahora vamos a guardar la información en una variable:

```python

nombre = input("dime tu nombre: ")
print("Bienvenido", nombre)

```
