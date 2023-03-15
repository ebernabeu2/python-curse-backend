from jornadaLaboral import JornadaLaboral


def main():
    horaSalida = JornadaLaboral(19)
    esHorarioLaboral = horaSalida.esHorarioLaboral()

    if esHorarioLaboral == 0:
        print('Es horario laboral. Quedan', round(horaSalida.tiempoFinJornada()/3600,1), 'horas para finalizar')
    else:
        print("Ahora no es horario laboral")


if __name__ == "__main__":
    main()
