import os, sys
from cx_Freeze import setup, Executable

files = [
    'interface/res/add_acc.svg',
    'interface/res/copy.svg',
    'interface/res/icon.ico',
    'interface/res/icon.png',
    'interface/res/login_acc.svg',
    'interface/res/manage_acc.svg'
]

target = Executable(
    script = 'main.py',
    base = 'Win32GUI',
    icon = 'interface/res/icon.ico',   
)

setup(
    name = 'League Account Manager',
    version = '0.0.1',
    description = 'Account manager for League of Legends.',
    author = 'Gabriel Viana',
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)