# Creemos una calculadora de comisiones
Hola autoestopista, hoy me acompañaras a crear una calculadora de comisiones para que los empleados de la empresa Veterinaria en redes sepan cuantas comisiones han ganado este mes por la venta de sus servicios.

## Repaso sobre tipos de datos en Python
| Tipo de datos | Descripción |
| ------------- | ------------- |
| string (str) | "Hola","%€&","123" Siempre van entre "" o si es un char '' |
| integer (int)  | 150, 42, -55, 0 Van sin commillas y podemos realizar operaciones aritméticas. |
| floating (float)  | 1.25, -2.67, 541.467 Tambien van sin commillas y se pueden emplear para realizar operaciones aritméticas |
| listas (list) | Se trata de una colección ordenada de objetos (cualquier tipo de dato) ["hola",42,-2.67,"%€&"], su orden lo determina su índice que va desde el 0 hasta n. siendo "hola" el índice 0 y "%€&" el índice 3. Siempre van entre [] y concatenados con una ",".|
| diccionarios(dic) | Consisten entre pares de palabras agrupados que van escritos entre {}, se concatenan con ",", cada par contiene dos elementos, una clave y un valor que se concatenan con ":" {'color':'rosa','arte':'creatividad'} si pensamos en un diccionario convencional equivaldria a una palabra y su definición. :exclamation: los pares no estan ordenados con un índice como pasa con las listas. |
| tuples (tuple) | Son un conjunto ordenado de elementos(cualquier tipo de dato), también va ordenado por índices, la mayor diferencia con las listas es que su orden es inmutable. Van escritos entre () y se concatenan ",". ('jan','feb','mar','apr'). |
| sets (set) | Se trata de un conjunto ordenado de elementos únicos , tanto listas como tuplas pueden tener elementos repetidos, pero en sets no pasa eso ya que cada elemento es único e irrepetible, van entre {} y concatenados "," {'a','b','c'} |
| booleanos (bool) | Son valores lógicos sencillos ya que solo tienen dos valores, verdadero o falso, lo vamos a emplear cuando necesitemos que en nuestro código tome decisiones, es decir si una condición se cumple o no: True, False  |
