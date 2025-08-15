import customtkinter as ctk
from sistema import *
from usuario import *


def rodar_programa():
    # Definindo cor da janela
    ctk.set_appearance_mode("dark")

    # Crianção da janela 
    janela = ctk.CTk()
    janela.title("Sistema de Login")
    janela.geometry("450x400")
    janela.maxsize(
        width=450, 
        height=400
    )
    janela.minsize(
        width=450, 
        height=400
    )


    # Criando as abas principais
    abas = ctk.CTkTabview(
        janela, 
        corner_radius=15
    )
    abas.pack()

    abas.add("Login")
    abas.add("Cadastrar Usuários")
    abas.add("Listar Usuários")
    abas.add("Sobre")

    # Frame para organizar tudo com grid
    ctk.CTkLabel(
        master=abas.tab("Login"), 
        text="LOGIN", 
        font=("bold", 15)
    ).pack()

    frame_login = ctk.CTkFrame(
        master=abas.tab("Login"),
        fg_color="transparent"
    )
    frame_login.pack(
        pady=30
        )

    # Função Login
    def login():
        email = entry_login.get().strip()
        senha = entry_senha.get().strip()
        if not email or not senha:
            msg_falha.configure(
                text="Favor preencher todos os campos!"
            )
            msg_falha.after(3000, lambda: msg_falha.configure(text=""))
        else:
            user = SistemaUsuarios()
            dados_usuario = user.autenticar_usuario(email, senha)
            entry_login.delete(0, "end")
            entry_senha.delete(0, "end")

            if dados_usuario:
                msg_sucesso.configure(
                    text="Login realizado com sucesso!"
                )
                msg_sucesso.after(3000, lambda: msg_sucesso.configure(text=""))
                # Nova janela 
                nova_janela = ctk.CTkToplevel(
                    janela
                    )
                nova_janela.title("Dados do Usuário")
                nova_janela.geometry("300x200")
                caixa_usuario = ctk.CTkTextbox(
                    nova_janela,
                    width=280,
                    height=150,
                )
                caixa_usuario.grid(
                    row=1,
                    column=0,
                    padx=10,
                    pady=5
                )

                caixa_usuario.insert("1.0", f"Nome: {dados_usuario['nome']}\n")
                caixa_usuario.insert("end", f"E-mail: {dados_usuario['email']}\n")
                caixa_usuario.configure(state="disabled")  # Impede edição
            else:  # Login falhou
                msg_falha.configure(
                    text="E-mail ou senha incorretos!"
                )
                msg_falha.after(3000, lambda: msg_falha.configure(text=""))
                

    
    # Mensagem falha e sucesso
    msg_sucesso = ctk.CTkLabel(
        master=abas.tab("Login"),
        text="",
        text_color="green"
    ) 
    msg_sucesso.pack(
        pady=5
        )

    msg_falha = ctk.CTkLabel(
        master=abas.tab("Login"),
        text="",
        text_color="red"
    )
    msg_falha.pack(
        pady=5
        )


    # ==== Linha 1: Login ====
    label_login = ctk.CTkLabel(
        master=frame_login,
        text="E-mail",
        width=100,
        anchor="e"
    )
    label_login.grid(
        row=0, 
        column=0, 
        padx=10,
        pady=5
    )
    
    entry_login = ctk.CTkEntry(
        master=frame_login,
        placeholder_text="Digite seu e-mail",
        width=250
    )
    entry_login.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
    )


    # ==== Linha 2: Senha ====
    label_senha = ctk.CTkLabel(
        master=frame_login,
        text="Senha",
        width=100,
        anchor="e"
    )
    label_senha.grid(
        row=1, 
        column=0, 
        padx=10,
        pady=5
    )
    
    entry_senha = ctk.CTkEntry(
        master=frame_login,
        show="*",
        placeholder_text="Digite sua senha",
        width=250
    )
    entry_senha.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
    )

    # Button: Login
    ctk.CTkButton(
        master=abas.tab("Login"),
        command=login,
        text="Entrar"
    ).pack()


    # Conteúdo da aba "Sobre"
    texto_sobre = (
        "🔐 Sistema de Login Seguro v1.0\n\n"
        "Desenvolvido por: Gabriel Brito\n"
        "Versão: 1.0\n"
        "Data: Agosto/2025\n\n"
        "Este sistema permite gerenciar o acesso de usuários\n"
        "de forma prática e segura, com autenticação baseada\n"
        "em credenciais armazenadas de forma protegida.\n\n"
        "Principais recursos:\n"
        "- Cadastro e login de usuários\n"
        "- Validação de credenciais\n"
        "- Interface moderna com CustomTkinter\n"
        "- Armazenamento seguro em JSON"
    )

    label_sobre = ctk.CTkLabel(
        abas.tab("Sobre"),
        text=texto_sobre,
        justify="left",
        font=ctk.CTkFont(size=14)
    )
    label_sobre.pack(padx=20, pady=20, anchor="center")


    janela.mainloop()


rodar_programa()