import os
from pathlib import Path

SUBDIRETORIOS={
    "DOCUMENTOS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png'],
    "PYTHON": ['.py'],
    "PHP": ['.php'],
}

def escolherDiretorio(valor):
    for categoria, extensoes in SUBDIRETORIOS.items():
        for extensao in extensoes:
            if extensao == valor:
                return categoria
    return 'MISTURADO'

def organizaDiretorio():
    for item in os.scandir():
        if item.is_dir():
            continue
        caminhoArquivo = Path(item)
        tipoArquivo = caminhoArquivo.suffix.lower()
        diretorio = escolherDiretorio(tipoArquivo)
        diretorioArquivo = Path(diretorio)

        if diretorioArquivo.is_dir() != True:
            diretorioArquivo.mkdir()
        
        caminhoArquivo.rename(diretorioArquivo.joinpath(caminhoArquivo))

organizaDiretorio()