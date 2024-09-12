import customtkinter as ctk
from random import randint
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """ Get absolut path to resource, woorks for dev and for PyInstaller """
    try: 
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Configuração do tema e aparência 
ctk.set_appearence_mode("System") # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")

# Inicializa a janela principal
root = ctk.CTk()
root.geometry("520x350")
root.title("Gerador de senha")

# Tenta carregar a imagem do ícone 
try:
    icon_path = resource_path("senha1.ico")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)
except Exception as e: 
    print(f"Não foi possível carregar o ícone: {e}")

# Função para gerar uma nova senha aleatória 
def new_rand():
    pw_entry.delete(0, ctk.END)
    pw_length = int(my_entry.get()) if my_entry.get() else 0
    my_password = ''.join(chr(randint(33, 126)) for _ in range(pw_length))
    pw_entry.insert(0, my_password)
    pw_entry.configure(justify='center')

# Função para copiar a senha gerada para a área de tranferência
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Função para limpar os campos de entrada 
def clear_entry():
    my_entry.delete(0, ctk.END)
    pw_entry.delete(0, ctk.END)
