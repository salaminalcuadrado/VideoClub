
import sys
sys.path.append('./tools')
sys.path.append('./control_libreria')

from agregar_modificar_clientes import modificar_client
from agregar_modificar_peliculas import modificar_peli
from peliculas import subir_alquiler


def alquiler_pelicula():

    cantidad = input(" ingrese la cantidad que alquilo de esta pelicula ")

    codigo_cliente = input(" ingrese el codigo del que alquilo la pelicula ")

    modificar_client(codigo_cliente)

    codigo_pelicula = input(
        " ingrese el codigo de la pelicula que se ha alquilado ")

    modificar_peli(codigo_pelicula)

    fecha = input(" ingrese la fecha cuando la/las alquilo ")

    data = {cantidad: {"codigo_cliente": codigo_cliente, "fecha": fecha}}

    subir_alquiler(data, codigo_pelicula)