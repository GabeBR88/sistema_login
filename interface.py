import customtkinter as ctk
from sistema import *
from usuario import *
import tkinter as tk

def rodar_programa():
    ctk.set_appearance_mode("dark")

    # Janela principal
    janela = ctk.CTk()
    janela.title("Sistema de Login")
    janela.geometry("450x400")
    janela.maxsize(width=450, height=400)
    janela.minsize(width=450, height=400)

    # Abas principais
    abas = ctk.CTkTabview(janela, corner_radius=15)
    abas.pack(fill="both", expand=True)

    abas.add("Login")
    abas.add("Cadastrar Usuários")
    abas.add("Listar Usuários")
    abas.add("Sobre")

    # ====================== ABA LOGIN ======================
    ctk.CTkLabel(master=abas.tab("Login"), text="LOGIN", font=("bold", 15)).pack(pady=10)

    frame_login = ctk.CTkFrame(master=abas.tab("Login"), fg_color="transparent")
    frame_login.pack(pady=10)

    # Mensagens de login
    msg_login_sucesso = ctk.CTkLabel(master=frame_login, text="", text_color="green")
    msg_login_sucesso.grid(row=2, column=0, columnspan=2, pady=2, sticky="nsew")

    msg_login_falha = ctk.CTkLabel(master=frame_login, text="", text_color="red")
    msg_login_falha.grid(row=3, column=0, columnspan=2, pady=2, sticky="nsew")

    # Campos de login
    ctk.CTkLabel(master=frame_login, text="E-mail", width=100, anchor="e").grid(row=0, column=0, padx=10, pady=5)
    entry_login = ctk.CTkEntry(master=frame_login, placeholder_text="Digite seu e-mail", width=250)
    entry_login.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(master=frame_login, text="Senha", width=100, anchor="e").grid(row=1, column=0, padx=10, pady=5)
    entry_senha = ctk.CTkEntry(master=frame_login, show="*", placeholder_text="Digite sua senha", width=250)
    entry_senha.grid(row=1, column=1, padx=10, pady=5)

    def login():
        email = entry_login.get().strip()
        senha = entry_senha.get().strip()
        if not email or not senha:
            msg_login_falha.configure(text="Favor preencher todos os campos!")
            msg_login_falha.after(3000, lambda: msg_login_falha.configure(text=""))
            return

        user = SistemaUsuarios()
        dados_usuario = user.autenticar_usuario(email, senha)
        entry_login.delete(0, "end")
        entry_senha.delete(0, "end")

        if dados_usuario:
            msg_login_sucesso.configure(text="Login realizado com sucesso!")
            msg_login_sucesso.after(3000, lambda: msg_login_sucesso.configure(text=""))

            nova_janela = ctk.CTkToplevel(janela)
            nova_janela.title("Dados do Usuário")
            nova_janela.geometry("300x200")

            caixa_usuario = ctk.CTkTextbox(nova_janela, width=280, height=150)
            caixa_usuario.grid(row=0, column=0, padx=10, pady=5)
            caixa_usuario.insert("1.0", f"Bem vindo(a)!\n")
            caixa_usuario.insert("2.0", f"Nome: {dados_usuario['nome']}\n")
            caixa_usuario.insert("end", f"E-mail: {dados_usuario['email']}\n")
            caixa_usuario.configure(state="disabled")
        else:
            msg_login_falha.configure(text="E-mail ou senha incorretos!")
            msg_login_falha.after(3000, lambda: msg_login_falha.configure(text=""))

    ctk.CTkButton(master=frame_login, text="Entrar", command=login, width=150).grid(row=4, column=0, columnspan=2, pady=10)

    # ====================== ABA CADASTRO ======================
    ctk.CTkLabel(master=abas.tab("Cadastrar Usuários"), text="CADASTRAR USUÁRIO", font=("bold", 15)).pack(pady=10)

    frame_cadastro = ctk.CTkFrame(master=abas.tab("Cadastrar Usuários"), fg_color="transparent")
    frame_cadastro.pack(pady=10)

    # Mensagens cadastro
    msg_cadastrar_sucesso = ctk.CTkLabel(master=frame_cadastro, text="", text_color="green")
    msg_cadastrar_sucesso.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")

    msg_cadastrar_falha = ctk.CTkLabel(master=frame_cadastro, text="", text_color="red")
    msg_cadastrar_falha.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

    # Campos de cadastro
    ctk.CTkLabel(master=frame_cadastro, text="Nome", width=100, anchor="e").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu nome", width=250)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(master=frame_cadastro, text="E-mail", width=100, anchor="e").grid(row=1, column=0, padx=10, pady=5)
    entry_email = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu e-mail", width=250)
    entry_email.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(master=frame_cadastro, text="Senha", width=100, anchor="e").grid(row=2, column=0, padx=10, pady=5)
    entry_s_senha = ctk.CTkEntry(master=frame_cadastro, show="*", placeholder_text="Digite sua senha", width=250)
    entry_s_senha.grid(row=2, column=1, padx=10, pady=5)

    ctk.CTkLabel(master=frame_cadastro, text="Confirme Senha", width=100, anchor="e").grid(row=3, column=0, padx=10, pady=5)
    entry_confirm_senha = ctk.CTkEntry(master=frame_cadastro, show="*", placeholder_text="Confirme sua senha", width=250)
    entry_confirm_senha.grid(row=3, column=1, padx=10, pady=5)

    def cadastrar_usuario():
        nome = entry_nome.get().title().strip()
        email = entry_email.get().strip()
        senha = entry_s_senha.get().strip()
        confirm_senha = entry_confirm_senha.get().strip()

        if senha != confirm_senha:
            msg_cadastrar_falha.configure(text="As senhas não conferem!")
            msg_cadastrar_falha.after(3000, lambda: msg_cadastrar_falha.configure(text=""))
            return
        
        if not nome or not email or not senha:
            msg_cadastrar_falha.configure(text="Favor preencher todos os campos!")
            msg_cadastrar_falha.after(3000, lambda: msg_cadastrar_falha.configure(text=""))
            return

        usuario = Usuario(nome, email)
        cadastro = SistemaUsuarios()
        sucesso, mensagem = cadastro.cadastrar_usuario(usuario, senha)

        if sucesso:
            msg_cadastrar_sucesso.configure(text=mensagem)
            msg_cadastrar_sucesso.after(3000, lambda: msg_cadastrar_sucesso.configure(text=""))
            entry_nome.delete(0, "end")
            entry_email.delete(0, "end")
            entry_s_senha.delete(0, "end")
            entry_confirm_senha.delete(0, "end")
        else:
            msg_cadastrar_falha.configure(text=mensagem)
            msg_cadastrar_falha.after(3000, lambda: msg_cadastrar_falha.configure(text=""))

    ctk.CTkButton(master=frame_cadastro, text="Cadastrar", command=cadastrar_usuario, width=150).grid(row=4, column=0, columnspan=2, pady=10)

    # ====================== ABA LISTAR =====================
    frame_listar = ctk.CTkFrame(master=abas.tab("Listar Usuários"))
    frame_listar.pack(padx=10, pady=10, fill="both", expand=True)  # usa pack aqui

    # Listbox com scrollbar (usando Listbox nativo)
    scrollbar = ctk.CTkScrollbar(master=frame_listar, orientation="vertical")
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(frame_listar, width=42, height=15)
    listbox.pack(side="left", fill="y")

    scrollbar = tk.Scrollbar(frame_listar, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    def listar_user():
        sistema = SistemaUsuarios()
        dados = sistema.listar_usuarios()

        listbox.delete(0, tk.END)  # limpa antes de mostrar

        if dados:
            for usuario in dados:
                listbox.insert(tk.END, f"{usuario['nome']} - {usuario['email']}")
        else:
            listbox.insert(tk.END, "Nenhum usuário cadastrado.")

    def excluir_usuario():
        selecionado = listbox.curselection()  # retorna tupla de índices
        if not selecionado:
            return

        idx = selecionado[0]
        item = listbox.get(idx)
        nome, email = item.split(" - ")

        sistema = SistemaUsuarios()
        sistema.excluir_usuario(email)
        listar_user()

    # Botões dentro do mesmo frame
    btn_listar = ctk.CTkButton(frame_listar, text="Listar Usuários", command=listar_user, width=100)
    btn_listar.pack(pady=5)

    btn_excluir = ctk.CTkButton(frame_listar, text="Excluir Usuário", command=excluir_usuario, width=100)
    btn_excluir.pack(pady=5)

    # ====================== ABA SOBRE ======================
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
    ctk.CTkLabel(abas.tab("Sobre"), text=texto_sobre, justify="left", font=ctk.CTkFont(size=14)).pack(padx=20, pady=20, anchor="center")

    janela.mainloop()



