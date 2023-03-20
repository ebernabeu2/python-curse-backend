from functools import reduce

lista = list(range(15))

filtrada = tuple(filter(lambda x: x %2, lista))

suma = reduce(lambda a,b: a+b, filtrada)

print(filtrada)
print(suma)