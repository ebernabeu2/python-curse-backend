def escribe(fichero, datos):
    f = open(fichero, 'a+')

    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'

        f.writelines(linea)
        f.readline()

    print(f.readline())

    f.close()

linea1 = ['En un lugar de la Mancha, ']
linea2 = ['de cuyo nombre no quiero acordarme']

escribe('mifichero.txt', linea1)
escribe('mifichero.txt', linea2)
