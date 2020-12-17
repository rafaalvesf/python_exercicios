import os

for raiz, diretorios, arquivos in os.walk('c:/Users/rafael.ferreira/Desktop/phyton/testePY'):
    for arquivo in arquivos:
        if arquivo.endswith('.zip'):
           os.remove(os.path.join(raiz, arquivo))