# ACCION 4


import sys
sys.path.append('./control_libreria')
sys.path.append('./tools')


from clientes import subir_diccionario, encontrar_codigo_clientes
from generar_datos import generar_data
from agregar_modificar_clientes import agregar_client


def agregar_a_clientes():

    codigo = input(" Ingrese el codigo del nuevo cliente ")

    codigo = agregar_client(codigo)

    datos = clientes()

    return subir_diccionario(datos, codigo)


def clientes():

    campos = [
        {
            "label": "nombre",
            "type": "string"
        },
        {
            "label": "fecha de alta (dd/mm/aaaa)",
            "type": "string",
            "key": "fecha_alta"
        },
        {
            "label": "telefono",
            "type": "string"
        },
        {
            "label": "mail",
            "type": "string"
        },
        {
            "label": "direccion",
            "type": "string"
        }
    ]

    return (generar_data(campos))
