import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("RADIOBUTTONS")
window.geometry('200x100')

def reset(event):
    print('Reset ok')
    selected.set("0")

def salir(event):
    print('exit')
    window.quit()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='No se', value='3', variable=selected)

r1.grid(column=1, row=1, sticky='w')
r2.grid(column=1, row=2, sticky='w')
r3.grid(column=1, row=3, sticky='w')

botonReset = tkinter.Button(window, text='Click para Reset')
botonReset.grid(column=2, row=0, rowspan=4, sticky='ns')
botonReset.bind('<Button-1>', reset)

botonSalir = tkinter.Button(window, text='Exit')
botonSalir.grid(column=0, row=40, columnspan=4, sticky='we')
botonSalir.bind('<Button-1>', salir)

window.mainloop()