from tkinter import *
from pickle import *
from os import path
from .user import User

class SignUpPage(Tk):

    PADX = 10
    PADY = 10
    FONT = ("TimesNewRoman", "14", "bold")
    BG = 'gray60'

    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)
        self.title = "Sign up"
        self.geometry("350x450")
        self.config(bg=self.BG)

        title_label = Label(self, text="Cadastre-se", padx=20, pady=15, font=self.FONT, bg=self.BG)
        title_label.pack()

        # Campo do nome
        self.name_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.name_frame.pack()

        self.name_label = Label(self.name_frame, text="Nome", font=self.FONT, bg=self.BG)
        self.name_label.pack(side=LEFT)

        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side=LEFT)

        # Campo de data de nascimento
        self.birth_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.birth_frame.pack()

        self.birth_label = Label(self.birth_frame, text="Data nascimento", font=self.FONT,bg=self.BG)
        self.birth_label.pack(side=LEFT)

        self.birth_entry = Entry(self.birth_frame)
        self.birth_entry.pack(side=LEFT)

        # Campo do email
        self.email_frame = Frame(self, padx=self.PADX, pady=self.PADY,bg=self.BG)
        self.email_frame.pack()

        self.email_label = Label(self.email_frame, text="Email", font=self.FONT, bg=self.BG)
        self.email_label.pack(side=LEFT)

        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)

        # Campo da senha
        self.password_frame = Frame(self, padx=self.PADX, pady=self.PADY, bg=self.BG)
        self.password_frame.pack()

        self.password_label = Label(self.password_frame, text="Senha", font=self.FONT, bg=self.BG)
        self.password_label.pack(side=LEFT)

        self.password_entry = Entry(self.password_frame, show='*')
        self.password_entry.pack(side=LEFT)

        # Confirmar senha
        self.conf_password_frame = Frame(self, padx=self.PADX, pady=self.PADY, bg=self.BG)
        self.conf_password_frame.pack()

        self.conf_password_label = Label(self.conf_password_frame, text="Confirme a senha", font=self.FONT, bg=self.BG)
        self.conf_password_label.pack(side=LEFT)

        self.conf_password_entry = Entry(self.conf_password_frame, show='*')
        self.conf_password_entry.pack(side=LEFT)
        
        # Botão de ação e mensagens
        self.confim_frame = Frame(self, bg=self.BG)
        self.confim_frame.pack()

        self.confirm_button = Button(self.confim_frame, text="Cadastrar", font=self.FONT, bg='gray65')
        self.confirm_button["command"] = self.validate
        self.confirm_button.pack()

        self.messages_label = Label(self.confim_frame, text="", font=self.FONT, bg='gray60')
        self.messages_label.pack() 

        self.mainloop()

    def validate(self) -> None:
            if path.exists("usuarios.txt"):
                try:
                    with open("usuarios.txt", "rb") as archive:
                        users = [x.email for x in load(archive)]
                except EOFError:
                    users = []
                    self.data = users
                    self.save(users)
            else:
                users = []

            if self.name_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "" or self.password_entry.get() == "" or self.conf_password_entry.get() == "":
                self.messages_label["text"] = "Campo inválido"

            elif self.password_entry.get() != self.conf_password_entry.get():
                self.messages_label["text"] = "As senhas não batem"
            elif self.email_entry.get() in users:
                self.messages_label["text"] = "Email já pertence a um usuário"
            else:
                self.messages_label["text"] = ""
                user = User(self.name_entry.get(), self.birth_entry.get(), self.email_entry.get(), self.password_entry.get())
                self.save(user)
                self.mostra_usuarios()


    def save(self, user: User) -> None:
        try:
            with open("usuarios.txt", "rb") as archive:
                self.data = load(archive)
                self.data.append(user)

        except EOFError:
            with open("usuarios.txt", "wb") as archive:
                dump(self.data, archive)

        with open("usuarios.txt", "wb") as archive:
                dump(self.data, archive)
        self.messages_label["text"] = "Usuário cadastrado"

    def mostra_usuarios(self):
        with open("usuarios.txt", "rb") as archive:
            for user in load(archive):
                print(user.name)