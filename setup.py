#python setup.py build

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Exec",
    options = options,
    version = "0.1",
    description = 'first attempt',
    executables = executables
)
