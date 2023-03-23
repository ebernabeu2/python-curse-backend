import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("RADIOBUTTONS")
window.geometry('200x150')


def salir(event):
    print('exit')
    window.quit()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)

labelTitulo = ttk.Label(window, text='¿Te gusta hacer deporte?')
labelTitulo.grid(column=0, row=0, sticky='w', columnspan=3, padx=5)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='A veces', value='3', variable=selected)

r1.grid(column=1, row=1, sticky='w')
r2.grid(column=1, row=2, sticky='w')
r3.grid(column=1, row=3, sticky='w')


botonSalir = tkinter.Button(window, text='Exit')
botonSalir.grid(column=0, row=40, columnspan=4, sticky='we')
botonSalir.bind('<Button-1>', salir)

window.mainloop()