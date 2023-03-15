from jornadaLaboral import JornadaLaboral


def main():
    horaSalida = JornadaLaboral(19)
    esHorarioLaboral = horaSalida.esHorarioLaboral()

    if esHorarioLaboral == 0:
        print(f'Es horario laboral. Quedan {round(horaSalida.tiempoFinJornada()/3600,1)} horas para finalizar')
    else:
        print(f'Ahora no es horario laboral')


if __name__ == "__main__":
    main()
