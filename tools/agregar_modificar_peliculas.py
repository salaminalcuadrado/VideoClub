import sys
sys.path.append('./control_libreria')

from peliculas import encontrar_codigo


def agregar_peli(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo(codigo)
        if buscar != None:
            codigo = input(" ingrese el codigo nuevamente porque ya existe")

        else:
            funciona = True


def modificar_peli(codigo):
    funciona = False
    while funciona == False:
        buscar = encontrar_codigo(codigo)
        if buscar == None:
            codigo = input(
                " ingrese el codigo nuevamente porque no se encuentra ")

        else:
            funciona = True