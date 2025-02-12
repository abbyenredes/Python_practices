# Python_practices
# Intro python

> Creemos un nuevo directorio: `mkdir intro_python`

> Abrimos la carpeta: `cd intro_python`

> comprobamos que versión de python tenemos `python3 --version`

Y creamos un entorno virtual: 
> Primero generemos la carpeta .venv `python3 -m venv .venv`

> Activamos `source .venv/bin/activate`

> [TIP!]
> crear un archivo de requerimientos en el que pondremos las librerias que vamos a usar. Ten encuenta que esta carpeta no puede ir dentro de la .venv.

> Crea tu archivo `vim requirements.txt` agrega `pandas` `notebook` y ejecutamos: `pip install -r requirements.txt`

> [TIP!]
> puedes usar uv para hacer esto mas rapido: `uv pip install -r pip requirements.txt`
> para descargar uv en tu entorno [UV](https://github.com/astral-sh/uv)
