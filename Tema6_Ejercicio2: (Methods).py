class Alumno:
    def inicializar (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir (self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def Resultado (self):
        if self.nota>=5:
            print("Aprobado")
        else:
            print("Suspenso")

alumno = Alumno()
alumno.inicializar("Alberto", 8)
alumno.imprimir()
alumno.Resultado()
