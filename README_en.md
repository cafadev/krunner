
# Krunner

[Documentación en español](https://github.com/kershingf/krunner/blob/master/README.md)

Krunner is a complement developed to compile and execute code from sublime text 3 with a simple combination of keys and auxiliary of the `* .sublime-project` files provided by the editor.
Krunner is in the alpha state and currently only allows interpretation of Python code, in future versions it includes support for Java projects, c ++, c, ruby among others.

## Supported Terminals
Krunner can execute your project with the following terminals:

 - deepin-terminal (Deepin Terminal)
 - gnome-terminal (Gnome Terminal)
 - xcfe4-terminal (XFCE Terminal)
 - konsole (KDE terminal)
 - xterm

## Standard Structure of the `.sublime-project` File
The `.sublime-project` files is the form used by sublime text to generate a workspace or project. You can find more information about this topic [here](https://www.sublimetext.com/docs/3/projects.html). This would be a properly created `.sublime-project` file:

    {
		"folders": [
			{"path": "."}
		]
	}
this is where Krunner comes into play by using three main keys,
however, each language can add more keys for its use. This would be a standard configuration for krunner:

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

## Python Structure of the `.sublime-project` File
Below the structure of a simple Python project:

    - My Project
	    - settings.sublime-project
	    - main.py
For the previous example, the structure of the `settings.sublime-project` file would be the following:

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
The python module also gives you the freedom to work with virtual environments, to use this quality you just have to indicate the path of the `bin /` folder of your virtual environment, as shown in the following example:

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
