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
## Creemos un programa simple con lo aprendido
Vamos a crear el nombre de una marca usando dos palabras, entre los requisitos esta que este entre comillas y haya un salto de linea:

Primero creare un mensaje para el usuario: 
```python

print("Bienvenido, te voy a ayudar a crear un nombre único para tu marca")

```
Después agregaré las 2 variables en las que se guarde la información del nombre y sus respectivas preguntas:
```python

print("Bienvenido, te voy a ayudar a crear un nombre único para tu marca")
animal = input("Dime un animal que te inspire: ")
adjetivo = input("Dime un adjetivo que describa tu momento favorito: ")
```
Por último nos queda mostrar el resultado en pantalla:
```python

print("Bienvenido, te voy a ayudar a crear un nombre único para tu marca")
animal = input("Dime un animal que te inspire: ")
adjetivo = input("Dime un adjetivo que describa tu momento favorito: ")
"¡Enhorabuena!\n El nombre de tu negocio es: " "\"",animal, adjetivo,"\"")
```
### Resultado:
![](https://github.com/abbyenredes/Python_practices/blob/main/01_generador_nombres/readme_files/01.gif)
