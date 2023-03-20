lista = input('Introduzca paises separados por comas: ').split(",")
print(f'Los paises que ha introducido, ordenados alfabeticamente, son:\n {",".join(sorted(set(lista)))}')