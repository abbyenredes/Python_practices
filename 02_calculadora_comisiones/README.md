# Creemos una calculadora de comisiones
Hola autoestopista, hoy me acompañaras a crear una calculadora de comisiones para que los empleados de la empresa Veterinaria en redes sepan cuantas comisiones han ganado este mes por la venta de sus servicios.

## Repaso sobre tipos de datos en Python
| Tipo de datos | Descripción |
| ------------- | ------------- |
| string (str) | "Hola","%€&","123" Siempre van entre "" o si es un char '' |
| integer (int)  | 150, 42, -55, 0 Van sin commillas y podemos realizar operaciones aritméticas. |
| floating (float)  | 1.25, -2.67, 541.467 Tambien van sin commillas y se pueden emplear para realizar operaciones aritméticas |
| listas (list) | Se trata de una colección ordenada de objetos (cualquier tipo de dato) ["hola",42,-2.67,"%€&"], su orden lo determina su índice que va desde el 0 hasta n. siendo "hola" el índice 0 y "%€&" el índice 3. Siempre van entre [] y concatenados con una ",".|
| diccionarios(dic) | Consisten entre pares de palabras agrupados que van escritos entre {}, se concatenan con ",", cada par contiene dos elementos, una clave y un valor que se concatenan con ":" {"color":"rosa","arte":"creatividad"} si pensamos en un diccionario convencional equivaldria a una palabra y su definición. :exclamation: los pares no estan ordenados con un índice como pasa con las listas. |
| tuples (tuple) | Son un conjunto ordenado de elementos(cualquier tipo de dato), también va ordenado por índices, la mayor diferencia con las listas es que su orden es inmutable. Van escritos entre () y se concatenan ",". ('jan','feb','mar','apr'). |
| sets (set) | Se trata de un conjunto ordenado de elementos únicos , tanto listas como tuplas pueden tener elementos repetidos, pero en sets no pasa eso ya que cada elemento es único e irrepetible, van entre {} y concatenados "," {'a','b','c'} |
| booleanos (bool) | Son valores lógicos sencillos ya que solo tienen dos valores, verdadero o falso, lo vamos a emplear cuando necesitemos que en nuestro código tome decisiones, es decir si una condición se cumple o no: True, False  |

## Repaso de variables
Me gusta pensar que las variables son cajas en las que almacenamos cosas, esas cosas son los tipos de datos anteriormente vistos. En programación una variable se trata de un espacio en la memoria reservado para guardar información que se va modificando dinamicamente.

Las variables se declaran de la siguiente manera:
``` python
mi_variable = "Bayta"
```
### Manual de buenas prácticas para nombrar variables:
1. Legible: debes elegir un nombre que describa lo que contiene tu variable para que tu código se legible.
2. Unidad: con el fin de ser mas descriptivos escribiremos nuestra variable seguida de _ ```numero_cuenta```.
3. Hispanismo: :shipit: no sabemos si en el futuro nuestro código sea utilizado o analizado, por ello es preferible escribirlo en inglés para que sea estandar.
4. Números: siempre después de una palabra ya que el compilador lo tomará como un error :x: ```2_funcion``` :white_check_mark: ```funcion_2```.
5. Signos: Tus nombre de variebles no deben contener ninguno de estos signos: :",<>/?|\\()!'@#$%^&*~-+
6. Palabras clave: No podremos usar palabras clave reservadas por el propio sistema, tales como: `['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']` Lo que si podemos usar es la palabra clave seguida de otra cosa: ```my_print``` ```int_total```

## Usando números
Aquí te daré tips para que uses el tipo de dato númerico ideal para tu programa.
Usaremos int en caso de manejar valores como edades, cantidades de personas, números de dias, posiciones en una lista....
``` python
edad = 42
poblacion = 3000054
dias_restantes = 5
n_clientes = 635
```
Usaremos float si mis valores son temperaturas, precios, pesos y medidas...
``` python
grados = -3.5
valor = 65.71
altura = 1.76
```
## Convirtiendo tipos de datos
> [!TIP]
>
> Para conocer el tipo de dato que tenemos podemos recurrir a la función ```type```
``` python
edad = 42
print(type(edad))
```
 ### Conversión implícita
 python convierte el tipo de dato de forma automatica:
 
 ``` python
precio_manzana = 2.30
precio_pera = 1
print(type(precio_manzana + precio_pera))
```
el resultado es 3.3, si ponemos type en ese print nos diria que es un float
al igual que si usasemos input su entrada convierte todo en str.

### Conversión explícita
Aquí le decimos a python en que tipo de dato queremos que se convierta:
 ``` python
edad = input("Dime tu edad: ")
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print("tu nueva edad es: ", nueva_edad)
```
Como vemos en el ejemplo input convierte automaticamente a str la variable lo que no nos permite hacer operaciones aritméricas, por ello realizamos un cast que en programacion significa cambiar de dato. Al hacer esto ya podemos utilizar ese dato para realizar operaciones en este caso sumar 1.

## Formatear cadenas
Nos sirve para concatenar distintos tipos de datos sin tener que recurrir a cast ya que no seria del todo óptimo. Por ello usaremos la función ```format```:

 ``` python
nombre = "Rosa"
edad = 23
altura = 1.78
es_mayor_edad = True
print(f"hola {nombre} tienes {edad} mides {altura} y eres mayor de edad {es_mayor_edad}")
```

También hay otra forma de declarar esta función:
 ``` python
nombre = "Rosa"
edad = 23
altura = 1.78
print("hola {} tienes {} mides {}".format(nombre,edad,altura))
```
Personalmente me parece más estético la primera forma de declaración.

## Operadores matemáticos
Operaciones básicas:

``` python
x = 4
y = 6
print(f"la suma de {x} mas {y} es igual a {x+y}")
print(f"la resta de {x} menos {y} es igual a {x-y}")
print(f"la división de {x} entre {y} es igual a {x/y}")
print(f"la mutiplicación de {x} por {y} es igual a {x*y}")
```

Operaciones avanzadas:

``` python
x = 2
y = 7
# si queremos un número sin decimales
print(f"{x} dividido al piso {y} es igual a {x//y}")
# si queremos saber el módulo de una división (se usa para ver los números pares)
print(f"{x} módulo {y} es igual a {x%y}")
# Para conocer la potencia
print(f"{x} elevado {y} es igual a {x**y}")
# Para conocer una raiz cuadrada
print(f"la raiz cuadrada de {x} es igual a {x**0.5}")
```

### Redondeo
Para redondear usamos la función ```round``` 
Redondeo a número entero
``` python
resultado = round(9/7)
print(resultado)
```
Redondeo a 2 decimales
``` python
# round(número_a_redondear, decimales_que_visualizar)
valor = round(9.6546, 2)
print(valor)

```
## Vamos a crear la calculadora de comisiones
Para la empresa x nos han pedido que desarrollemos un programa que permita a los vendedores conocer su comisión mensual:
- Tiene que pedirle su nombre
- ¿Cuanto ha vendido este mes?
- Calcular comision venta * 13 / 100
- Da resultado: Ok (nombre) este mes ganaste (comision) €
- La comision debe esta redondeada a 2 decimales.

```python
nombre = input("Dime tu nombre: ")
venta_mes = float(input("Dime cuando has vendido este mes: "))
comision = venta_mes * 13 / 100
comision = round(comision, 2)
print(f"Ok {nombre} este mes ganaste {comision} €")
```
## Resultado
![Calculadora](https://github.com/abbyenredes/Python_practices/blob/main/02_calculadora_comisiones/img/02_calculadora.gif)
