from usuario import *
from utils import *
from pathlib import Path
import re

path = Path(r"E:\Workspace\Um treino por dia\AGOSTO\Projeto1\sistema_login\data\cadastro.json")

class SistemaUsuarios:
    def __init__(self):
        self.lista_usuarios = []

    
    def validar_email(self, email: str) -> bool:
        return re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email) is not None

    def validar_senha(self, senha: str) -> bool:
        return re.match(r"^.{6,}$", senha) is not None
    

    def cadastrar_usuario(self, usuario:Usuario):
        self.lista_usuarios.extend(carregar_json(path))

        if not self.validar_email(usuario.email):
            print("❌ E-mail inválido. Tente novamente!")
            return
            
        senha = input("Digite a senha: ")
        if not self.validar_senha(senha):
            print("❌ A senha deve ter pelo menos 6 caracteres.")
            return
            
        usuario.set_senha(senha)

        if usuario.verificar_senha(senha) == True:
            dados = {
                "nome" : usuario.nome,
                "email" : usuario.email,
                "senha" : usuario.senha_hash
            }

            self.lista_usuarios.append(dados)
            salvar_json(path, self.lista_usuarios)
            print("Salvo com sucesso!")
        
        else:
            print("Tente novamente!")


    def autenticar_usuario(self, email:str, senha:str):
        usuarios = carregar_json(path)
        if not usuarios:
            return None  # Não há usuários

        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha_hash:
                return usuario  # Retorna o dicionário com os dados do usuário

        return None  # Se não encontrar
            

    def listar_usuarios(self):
        usuarios = carregar_json(path)
        if not usuarios:
            print("Não há dados cadastrados!")
            return
        
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}\n")
           

