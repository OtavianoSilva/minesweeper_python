from tkinter import *

class Profile(Tk):
    
    PADX = 10
    PADY = 15
    FONT = ("TimesNewRoman", "14", "bold")
    BG = "gray60"

    def __init__(self, current_player) -> None:
        Tk.__init__(self)

        self.current_player = current_player

        self.title = "Profile"
        self.geometry("350x450")
        self.config(bg='gray60')

        self.main_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame, text="Perfil do usuário:", font=self.FONT, bg=self.BG)
        self.title_label.pack()

        self.name_label = Label(self.main_frame, text=f"{self.current_player.name}", font=self.FONT, bg=self.BG)
        self.name_label.pack()
        
        self.email_label = Label(self.main_frame, text=f"{self.current_player.email}", font=self.FONT, bg=self.BG)
        self.email_label.pack()

        for mode in self.current_player.bast_game:
            bast_game_label = Label(self.main_frame, 
            text=f"Melhor jogo {mode}\n {self.current_player.bast_game[mode]:.2f} minutos" if self.current_player.bast_game[mode] < 100000 else "Sem dados",
            font=self.FONT, bg=self.BG)
            bast_game_label.pack()

        self.edit_button = Button(self.main_frame, text="Editar informações", font=self.FONT, bg=self.BG)
        self.edit_button["command"] = self.set_edit_frame
        self.edit_button.pack()

        self.delete_button = Button(self.main_frame,text="Deletar conta", font=self.FONT, bg=self.BG)
        self.delete_button["command"] = self.delete_accunt
        self.delete_button.pack()

    def set_edit_frame(self) -> None:
        self.main_frame.destroy()

        name_entry_text = StringVar(self)
        name_entry_text.set(self.current_player.name)

        email_entry_text = StringVar(self)
        email_entry_text.set(self.current_player.email)

        birth_entry_text = StringVar(self)
        birth_entry_text.set(self.current_player.birth_date)

        password_entry_text = StringVar(self)
        password_entry_text.set(self.current_player.get_password())

        # Campos de nome
        self.name_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.name_frame.pack()

        self.name_label = Label(self.name_frame, text="Nome", font=self.FONT, bg=self.BG)
        self.name_label.pack(side=LEFT)

        self.name_entry = Entry(self.name_frame, textvariable=name_entry_text)
        self.name_entry.pack(side=LEFT)

        # Campo de data de nascimento
        self.birth_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.birth_frame.pack()

        self.birth_label = Label(self.birth_frame, text="Data nascimento", font=self.FONT,bg=self.BG)
        self.birth_label.pack(side=LEFT)

        self.birth_entry = Entry(self.birth_frame, textvariable=birth_entry_text)
        self.birth_entry.pack(side=LEFT)

        # Campo do email
        self.email_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.email_frame.pack()

        self.email_label = Label(self.email_frame, text="Email", font=self.FONT, bg=self.BG)
        self.email_label.pack(side=LEFT)

        self.email_entry = Entry(self.email_frame, textvariable=email_entry_text)
        self.email_entry.pack(side=LEFT)

        # Campo da senha
        self.password_frame = Frame(self, padx=self.PADX, pady=self.PADY, bg=self.BG)
        self.password_frame.pack()

        self.password_label = Label(self.password_frame, text="Senha", font=self.FONT, bg=self.BG)
        self.password_label.pack(side=LEFT)

        self.password_entry = Entry(self.password_frame, textvariable=password_entry_text)
        self.password_entry.pack(side=LEFT)
        
        # Botão de ação e mensagens
        self.confim_frame = Frame(self, bg=self.BG)
        self.confim_frame.pack()

        self.confirm_button = Button(self.confim_frame, text="Editar", font=self.FONT, bg='gray65')
        self.confirm_button["command"] = self.edit_infos
        self.confirm_button.pack()

        self.messages_label = Label(self.confim_frame, text="", font=self.FONT, bg='gray60')
        self.messages_label.pack()

    def edit_infos(self) -> None:
        self.current_player.edit_infos(self.name_entry.get(), self.birth_entry.get(),
                                       self.email_entry.get(), self.password_entry.get())
        
        self.messages_label["text"] = "Alterações salvas\nreinicie o sistema"

    def delete_accunt(self) -> None:
        self.current_player.delete()
        self.destroy()
    