from tkinter import *
from pickle import *

class User():
    def __init__(self, name, birth_date, email, password) -> None:
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.password = password


class SignUpPage(Tk):

    PADX = 10
    PADY = 10
    FONT = ("TimesNewRoman", "14", "bold")

    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)
        self.title = "Sign up"
        self.geometry("450x600")

        title_label = Label(self, text="Cadastre-se", padx=20, pady=15, font=self.FONT)
        title_label.pack()

        # Campo do nome
        self.name_frame = Frame(self, padx=self.PADX, pady=self.PADY)
        self.name_frame.pack()

        self.name_label = Label(self.name_frame, text="Nome", font=self.FONT)
        self.name_label.pack(side=LEFT)

        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side=LEFT)

        # Campo de data de nascimento
        self.birth_frame = Frame(self, padx=self.PADX, pady=self.PADY)
        self.birth_frame.pack()

        self.birth_label = Label(self.birth_frame, text="Data nascimento", font=self.FONT)
        self.birth_label.pack(side=LEFT)

        self.birth_entry = Entry(self.birth_frame)
        self.birth_entry.pack(side=LEFT)

        # Campo do email
        self.email_frame = Frame(self, padx=self.PADX, pady=self.PADY)
        self.email_frame.pack()

        self.email_label = Label(self.email_frame, text="Email", font=self.FONT)
        self.email_label.pack(side=LEFT)

        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)

        # Campo da senha
        self.password_frame = Frame(self, padx=self.PADX, pady=self.PADY)
        self.password_frame.pack()

        self.password_label = Label(self.password_frame, text="Senha", font=self.FONT)
        self.password_label.pack(side=LEFT)

        self.password_entry = Entry(self.password_frame, show='*')
        self.password_entry.pack(side=LEFT)

        # Confirmar senha
        self.conf_password_frame = Frame(self, padx=self.PADX, pady=self.PADY)
        self.conf_password_frame.pack()

        self.conf_password_label = Label(self.conf_password_frame, text="Confirme a senha", font=self.FONT)
        self.conf_password_label.pack(side=LEFT)

        self.conf_password_entry = Entry(self.conf_password_frame, show='*')
        self.conf_password_entry.pack(side=LEFT)
        
        # Botão de ação e mensagens
        self.confim_frame = Frame(self)
        self.confim_frame.pack()

        self.confirm_button = Button(self.confim_frame, text="Cadastrar", font=self.FONT)
        self.confirm_button["command"] = self.validate
        self.confirm_button.pack()

        self.messages_label = Label(self.confim_frame, text="", font=self.FONT)
        self.messages_label.pack() 

        self.mainloop()

    def validate(self) -> None:
        try:
            with open("usuarios.txt", "rb") as archive:
                lista = [x.email for x in load(archive)]
                if self.name_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "" or self.password_entry.get() == "" or self.conf_password_entry.get() == "":
                    self.messages_label["text"] = "Campo inválido"

                elif self.password_entry.get() != self.conf_password_entry.get():
                    self.messages_label["text"] = "As senhas não batem"
                elif self.email_entry.get() in lista:
                    self.messages_label["text"] = "Email já pertence a um usuário"
                else:
                    self.messages_label["text"] = ""
                    user = User(self.name_entry.get(), self.birth_entry.get(), self.email_entry.get(), self.password_entry.get())
                    self.save(user)
                    self.mostra_usuarios()

        except:
            with open("usuarios.txt", "wb") as archive:
                dump([], archive)


    def save(self, user: User) -> None:
        with open("usuarios.txt", "rb") as archive:
            self.data = load(archive)
            self.data.append(user)

        with open("usuarios.txt", "wb") as archive:
            dump(self.data, archive)

    def mostra_usuarios(self):
        with open("usuarios.txt", "rb") as archive:
            for user in load(archive):
                print(user.name)