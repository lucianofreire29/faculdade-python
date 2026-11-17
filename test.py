import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Cadastro de Clientes")
        self.geometry("900x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Barra lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        # Abas principais
        self.janela_abas = ctk.CTkTabview(self, width=400)
        self.janela_abas.grid(
            row=0, column=1, sticky="nsew", padx=10
        )

        self.janela_abas.add("Perfil")
        self.janela_abas.add("Preferências")
        self.janela_abas.add("Dashboard")

        self.construir_abalateral()
        self.construir_abaperfil()
        self.construir_abapreferencias()
        self.construir_abasistema()

    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(
            self.barra_lateral,
            text="Meu App",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.titulo.pack(pady=(30, 5), padx=20)

        self.subtitulo = ctk.CTkLabel(
            self.barra_lateral,
            text=""
        )
        self.subtitulo.pack(pady=(0, 5))

        self.botao_principal = ctk.CTkButton(
            self.barra_lateral,
            text="Dashboard Principal",
            command=self.ir_para_dashboard
        )
        self.botao_principal.pack(pady=30, padx=10)

        self.switch_mododark = ctk.CTkSwitch(
            self.barra_lateral,
            text="Modo Escuro",
            command=self.mudar_modo_dark
        )
        self.switch_mododark.pack(pady=10, side="bottom")
        self.switch_mododark.select()

    def construir_abaperfil(self):
        self.aba_perfil = self.janela_abas.tab("Perfil")

        # Campo de nome
        self.campo_nome = ctk.CTkEntry(
            self.aba_perfil,
            placeholder_text="Digite o seu nome",
            width=300
        )
        self.campo_nome.pack(pady=20)

        # Nível do usuário
        self.nivel_usuario = ctk.IntVar(value=0)

        self.radio_label = ctk.CTkLabel(
            self.aba_perfil,
            text="Nível Usuário"
        )
        self.radio_label.pack()

        self.radio_basico = ctk.CTkRadioButton(
            self.aba_perfil,
            text="Básico",
            variable=self.nivel_usuario,
            value=1
        )
        self.radio_basico.pack()

        self.radio_admin = ctk.CTkRadioButton(
            self.aba_perfil,
            text="Admin",
            variable=self.nivel_usuario,
            value=2
        )
        self.radio_admin.pack()

        # Notificações
        self.checkbox_notificacoes = ctk.CTkCheckBox(
            self.aba_perfil,
            text="Receber notificações por email"
        )
        self.checkbox_notificacoes.pack(pady=20)

        # Salvar perfil
        self.botao_salvarperfil = ctk.CTkButton(
            self.aba_perfil,
            text="Salvar Perfil",
            fg_color="green",
            hover_color="darkgreen",
            command=self.salvar_perfil
        )
        self.botao_salvarperfil.pack(pady=20)

    def construir_abapreferencias(self):
        self.aba_preferencias = self.janela_abas.tab("Preferências")

        self.label_idiomas = ctk.CTkLabel(
            self.aba_preferencias,
            text="Selecione o idioma"
        )
        self.label_idiomas.pack(pady=(20, 5))

        self.menu_idiomas = ctk.CTkOptionMenu(
            self.aba_preferencias,
            values=["Português", "Inglês", "Espanhol"]
        )
        self.menu_idiomas.pack()

        self.label_volume = ctk.CTkLabel(
            self.aba_preferencias,
            text="Volume do sistema"
        )
        self.label_volume.pack(pady=(30, 5))

        self.slider_volume = ctk.CTkSlider(
            self.aba_preferencias,
            from_=0,
            to=100,
            command=self.atualizar_volume
        )
        self.slider_volume.pack()
        self.slider_volume.set(50)

        self.label_valor_volume = ctk.CTkLabel(
            self.aba_preferencias,
            text="50%"
        )
        self.label_valor_volume.pack()

    def construir_abasistema(self):
        self.aba_sistema = self.janela_abas.tab("Dashboard")

        self.label_carregamento = ctk.CTkLabel(
            self.aba_sistema,
            text="Testar Carregamento do Sistema",
            font=ctk.CTkFont(size=16)
        )
        self.label_carregamento.pack(pady=30)

        self.barra_progresso = ctk.CTkProgressBar(
            self.aba_sistema,
            width=400
        )
        self.barra_progresso.pack(pady=10)
        self.barra_progresso.set(0)

        self.botao_progresso = ctk.CTkButton(
            self.aba_sistema,
            text="Iniciar Carregamento",
            command=self.carregar
        )
        self.botao_progresso.pack(pady=20)

    def ir_para_dashboard(self):
        self.janela_abas.set("Dashboard")

    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("System")

    def salvar_perfil(self):
        nome = self.campo_nome.get()

        if self.nivel_usuario.get() == 2:
            nivel = "Admin"
        else:
            nivel = "Básico"

        receber_notificacoes = self.checkbox_notificacoes.get()

        print("Nome:", nome)
        print("Nível:", nivel)
        print("Receber notificações:", receber_notificacoes)

        self.titulo.configure(text=f"{nome} App")
        self.subtitulo.configure(text=nivel)

    def atualizar_volume(self, novo_valor_volume):
        self.label_valor_volume.configure(
            text=f"{int(novo_valor_volume)}%"
        )

    def carregar(self):
        self.botao_progresso.configure(state="disabled")
        self.barra_progresso.set(0)
        self.atualizar_progresso(0)

    def atualizar_progresso(self, etapa):
        self.barra_progresso.set(etapa / 100)

        if etapa < 100:
            self.after(100, self.atualizar_progresso, etapa + 1)
        else:
            self.botao_progresso.configure(state="normal")


if __name__ == "__main__":
    janela = Aplicativo()
    janela.mainloop()