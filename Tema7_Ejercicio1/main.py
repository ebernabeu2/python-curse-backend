import operaciones as o


def main():
    a = 2
    b = 3
    resSuma = o.suma(a, b)
    resResta = o.resta(a, b)
    resProducto = o.producto(a, b)
    resDividir = o.dividir(a, b)
    print("El resultado de la suma es: ", resSuma)
    print("El resultado de la resta es: ", resResta)
    print("El resultado de la multiplicacion es: ", resProducto)
    print("El resultado de la division es: ", resDividir)


if __name__ == '__main__':
    main()