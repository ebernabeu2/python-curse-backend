import pickle

class Vehiculo:

    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

    def getNombre(self):
        return self.modelo, self.precio

j1 = Vehiculo("Golf",2500.0)

#guardo datos en disco serializados
f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close()

#leo los datos guardados
f = open('datos.bin', 'rb')
coche = pickle.load(f)
f.close()

print(type(coche))
print("modelo: ", coche.modelo, ", precio: ", coche.precio)