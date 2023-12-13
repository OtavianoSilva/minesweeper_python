from tkinter import *
from pickle import *
from os import path

if path.exists("usuarios.txt"):
    with open("usuarios.txt", "rb") as archive:
        x = load(archive)
        if x == None:
            print("nada")
