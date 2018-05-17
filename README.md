# Krunner

[English documentation](https://github.com/kershingf/krunner/blob/master/README_en.md)

Krunner es un plugin desarrollado para compilar y ejecutar codigo desde sublime text 3 con una simple combinación de teclas y auxiliandose de los archivos `*.sublime-project` proporcionados por el editor.
Krunner se encuentra en estado alfa y actualmente solo permite la interpretación de codigo Python, en futuras versiones se incluira soporte para proyectos java, c++, c, ruby entre otros.

## Terminales soportadas
Krunner puede ejecutar tu proyecto con las siguientes terminales:

 - deepin-terminal (Deepin Terminal)
 - gnome-terminal (Gnome Terminal)
 - xcfe4-terminal (XFCE Terminal)
 - konsole (KDE terminal)
 - xterm

## Estructura estandar del archivo `.sublime-project`
Los archivos `.sublime-project` es la forma que utiliza sublime text para generar un espacio de trabajo o proyecto. Puedes encontrar más información acerca de este tema [aquí](https://www.sublimetext.com/docs/3/projects.html). Este seria un archivo `.sublime-project` correctamente creado:

    {
		"folders": [
			{"path": "."}
		]
	}
es aquí donde Krunner entra en juego haciendo uso de tres llaves principales,
sin embargo cada lenguaje puede agregar mas llaves para su utilización. Esta seria una configuración estandar para krunner:

    {
		"folders": [
			{"path": "."}
	    ],
	    "krunner": {
		    "lang": "PROGRAMMING_LANGUAGE",
		    "main": "MAIN_FILE_TO_RUN",
		    "shell": "TERMINAL_TO_USE"
	    }
	}

## Estructura Python del archivo `.sublime-project`
A continuación la estructura de un proyecto sencillo en Python:

    - My Project
	    - settings.sublime-project
	    - main.py
Para el ejemplo anterior la estructura del archivo `settings.sublime-project` sería la siguiente:

    {
		"folders": [
			{"path": "."}
	    ],
	    "krunner": {
		    "lang": "python",
		    "main": "main.py",
		    "shell": "TERMINAL_TO_USE"
	    }
    }
El modulo de python tambien te da la libertad de trabajar con entornos virtuales, para utilizar esta cualidad solo debes de indicar la ruta de la carpeta `bin/` de tu entorno virtual, como se muestra en el siguiente ejemplo:

    {
		"folders": [
			{"path": "."}
	    ],
	    "krunner": {
		    "lang": "python",
		    "main": "main.py",
		    "shell": "TERMINAL_TO_USE",
		    "virtualenv": "/home/YOUR_USER/virtualenvs/VIRTUALENV_NAME/bin"
	    }
    }
