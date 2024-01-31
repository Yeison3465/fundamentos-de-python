
import tkinter as t
window = t.Tk()
texto=t.Label(
    text="Hola mundo",
    fg="green",
    bg="white", # color de fondo
    width=200,
    height=200,

)
texto.pack()
window=t.mainloop()
