from tkinter import *
import pygame

# Función para reproducir un sonido utilizando Pygame
def play_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()

# Función para crear un botón con un sonido asociado
def create_button(frame, text, file):
    btn = Button(frame, height=6, width=4, bd=4, text=text, 
                font=("arial", 18, "bold"), bg="black", fg="white", 
                command=lambda: play_sound(file))
    btn.pack(side=LEFT, padx=5, pady=5)
    return btn

# Inicializa Pygame para reproducir sonidos
pygame.init()

# Creación de la ventana principal
root = Tk()
root.title("Caja de Música")
root.geometry("1352x700+0+0")
root.configure(background="white")

# Marco principal
abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.pack()

# Marcos secundarios dentro del marco principal
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.pack()

abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.pack()

abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.pack()

# Definición de sonidos y etiquetas asociadas a los botones para Pygame
pygame_sounds = [
    ("Sol", "Sol.wav"),
    ("La", "La.wav"),
    ("Si", "Si.wav"),
    ("Do", "Do.wav"),
    ("Re", "Re.wav"),
    ("Mi", "Mi.wav"),
    ("Fa", "Fa.wav"),
    ("Sol", "Sol.wav"),
    ("La", "La.wav"),
    ("Si", "Si.wav"),
    ("Do", "Do.wav"),
    ("Re", "Re.wav"),
    ("Mi", "Mi.wav"),
    ("Fa", "Fa.wav"),
    ("Sol", "Sol.wav")
]

# Crea botones asociados a sonidos usando Pygame
for label, file in pygame_sounds:
    create_button(abc3, label, file)

# Definición de sonidos y etiquetas asociadas a los botones para la librería Tkinter
tkinter_sounds = [
    ("Sol#", "Sol#.wav"),
    ("La#", "La#.wav"),
    ("Do#", "Do#.wav"),
    ("Re#", "Re#.wav"),
    ("Fa#", "Fa#.wav"),
    ("Sol#", "Sol#.wav"),
    ("La#", "La#.wav"),
    ("Do#", "Do#.wav"),
    ("Re#", "Re#.wav"),
    ("Fa#", "Fa#.wav")
]


# Crea botones asociados a sonidos usando Tkinter
for label, file in tkinter_sounds:
    create_button(abc2, label, file)

# Etiqueta en el marco 1 (abc1) para mostrar el título
Label(abc1, text="Xiolofono Musical Llaves", font=("arial", 25, "bold"), padx=8, pady=8, bd=4, width=59, bg="powder blue", fg="white", height=1, justify=CENTER).pack()

# Variable para mostrar el estado actual o mensaje en el marco 1 (abc1)
str = StringVar()
str.set("Just like Music")

# Entrada en el marco 1 (abc1) para mostrar el estado o mensaje actual
display = Entry(abc1, textvariable=str, font=("arial", 18, "bold"), width=35, bd=34, bg="powder blue", fg="black", justify=CENTER)
display.pack(pady=1)

#Ejecutar
root.mainloop()
