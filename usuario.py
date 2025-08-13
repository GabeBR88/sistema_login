import hashlib

class Usuario:
    def __init__(self, nome:str, email:str):
        self.nome = nome
        self.email = email
        self.senha_hash = None

    
    def set_senha(self, senha_texto):
        self.senha_hash = hashlib.sha256(senha_texto.encode()).hexdigest()


    def verificar_senha(self, senha_texto):
        return hashlib.sha256(senha_texto.encode()).hexdigest() == self.senha_hash


