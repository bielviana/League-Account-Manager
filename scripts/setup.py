from os import system as cmd
cmd('cls')


def pip_install(lib=str) -> None:
    """Install the project required libraries.

    Args:
        lib (str, required): lib name on pypi. Defaults to str.
    """    
    cmd(f'pip install {lib}')

with open('requirements.txt', 'r') as file:
    req = file.readlines()

libs = 0
libs_log = []
for x in range(len(req)):
    try:
        pip_install(req[x])
        libs += 1
        libs_log.append(req[x].replace('\n', '... OK'))
    except:
        libs_log.append(req[x].replace('\n', '... ERROR!'))

cmd('cls')

if libs == len(req):
    print('All libraries were successfully installed!')
elif libs == 0:
    print('No libraries have been installed!')
else:
    print('One or more libraries were not installed!')

print('\n')

for x in range(len(libs_log)):
    print(libs_log[x])