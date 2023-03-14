#El calendario gregoriano estableció (1582) que un año es bisiesto si es divisible entre 4, a menos que sea divisible
# entre 100. Sin embargo, si un año es divisible entre 100 y además es divisible entre 400, también resulta bisiesto
year = int(input("Por favor, introduce un año: "))

def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 'es bisiesto'

    else:
        return 'no es bisiesto'

print(year,(bisiesto (year)))
