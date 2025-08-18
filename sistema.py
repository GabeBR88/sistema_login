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
    

    def cadastrar_usuario(self, usuario: Usuario, senha):
        self.lista_usuarios.extend(carregar_json(path))

        if not self.validar_email(usuario.email):
            return False, "E-mail inválido. Tente novamente!"
        
        if not self.validar_senha(senha):
            return False, "A senha deve ter pelo menos 6 caracteres."
            
        usuario.set_senha(senha)

        if usuario.verificar_senha(senha):
            dados = {
                "nome": usuario.nome,
                "email": usuario.email,
                "senha": usuario.senha_hash
            }
            self.lista_usuarios.append(dados)
            salvar_json(path, self.lista_usuarios)
            return True, "Usuário salvo com sucesso!"
        else:
            return False, "Erro ao verificar senha. Tente novamente!"


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
        return carregar_json(path)
    
    
    def excluir_usuario(self, email):
        usuarios = carregar_json(path)
        usuarios = [u for u in usuarios if u['email'] != email]  # remove o usuário
        salvar_json(path, usuarios)
        return True

        
           

