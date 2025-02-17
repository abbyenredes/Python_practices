# Python_practices
# Ejecutar django en un entorno virtual usando uv

Creamos una nueva carpeta que sera nuestro entorno virtua (carpeta madre), en este caso sera una tienda de libros

```plaintext
mkdir book_store
```
Accedemos a esta carpeta:

```plaintext
cd book_store
```
Creamos el entorno virtual usando uv:

```plaintext
uv venv .venv
```
Iniciamos ese entorno virtual:

```plaintext
source .venv/bin/activate
```
Iniciamos nuestro proyecto:

```plaintext
uv init --bare
```
Descargamos nuestra dependencia de django:

```plaintext
uv add django
```
Iniciamos el proyecto en django:

```plaintext
django-admin startproject book_manage .
```

Y por ultimo iniciamos la app:

```plaintext
 django-admin startapp books
```

Abrimos VS:

```plaintext
code .
```

## Configuracion
En la carpeta book_manage, en el archivo settings.py -> instale apps agregamos una linea para `"Books",`
