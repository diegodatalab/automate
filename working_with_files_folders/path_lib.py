""" 'pathlib' is a 'os' substitute's library, which treats file paths as strings
and Pathlib uses a path object type to represent paths
""" 
from pathlib import Path

arquivo2 = Path('working_with_files_folders/files/2.txt')

arquivo3 = Path('working_with_files_folders/files/3.txt')

# print(type(arquivo2))

# print(dir(Path))

if arquivo2.exists():
    with open(arquivo2, 'r') as file:
        print(file.read())

if not arquivo3.exists():
    with open(arquivo3, 'w') as file:
        file.write('whatever')
        
print(arquivo3.name)    # ! name of file with extension
print(arquivo3.stem)    # ! name of file without extension
print(arquivo3.suffix)  # ! only the extension


arquivos = Path('working_with_files_folders/files')
print(arquivos.iterdir())

for arquivo in arquivos.iterdir():
    print(arquivo)