from os import system
from struct import pack
system("cls")

# tiker siiiiii
import tkinter as t

app= t.Tk() # este la pantala del programa
palabra=t.StringVar(app)
entrada=t.StringVar(app)
# dimenciones de Anchura X Largura 
app.geometry("1920x1080")
# cambiar color 
app.configure(background="black")
# cambiar el titulo de la app
t.Wm.wm_title(app,"mi primer programa")

t.Button(
    app, 
    text="aprime aqui :)",
    font=("Arial",14),
    bg="#00a8e8",
    fg="white",
    command=lambda:print("Hola que tal " + entrada.get())
).pack(
    fill=t.BOTH,
    expand=True,
)
t.Entry(
    fg="white",
    bg="black",
    justify="center",
    textvariable=entrada,
).pack(
    fill=t.BOTH,
    expand=True,
)
app.mainloop() # este sirve para refrescar el programa 