### Organizador de Arquivos por Pasta

    No SUBDIRETORIOS você define o nome da pasta e as extensões que faram parte dela.

### Criando .exe do programa 

    Instale o pyinstaller

    pip install pyinstaller

    Execute o comando:

        pyinstaller -w -F Organiza.py

    Caso de algum erro, tenta usar esse comando e depois repetir o processo  anterior:

        pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

    
**Colocando para executar com botão direito do mouse**

1. Gere o exe.

```
pyinstaller -w -F Organiza.py

```

2. Adicione a chave ao regedit ou rode  *organiza.reg*.
3. Copie .exe no *C:\Program Files\Organiza*
4. adicione *C:\Program Files\Organiza* no *Path* do windows.

