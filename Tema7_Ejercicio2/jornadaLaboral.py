from time import localtime, time, mktime


class JornadaLaboral:
    def __init__(self, horaSalida):
        self.horaSalida = horaSalida


    def esHorarioLaboral(self):

        result = localtime()
        if self.horaSalida <= result.tm_hour:
            esHorario = 1
        else:
            esHorario = 0
        return esHorario


    def tiempoFinJornada(self):

        segundos = time()
        result = localtime()
        horarioFin = mktime((result.tm_year, result.tm_mon,
                            result.tm_mday, self.horaSalida, 0, 0, 0, 0, 0))
        return horarioFin-segundos