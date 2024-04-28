from fecha.gestorfecha import GestorFechas
from equipo.gestorequipo import GestorEquipos
if __name__=='__main__':
    gf=GestorFechas
    ge=GestorEquipos
    opcion=str(input("Elegir numero de opcion:\n1. Leer datos de los equipos.\n2. Leer datos de las fechas.\n3. Obtener datos de un equipo.\n4. Actualizar tabla de los equipos.\n5. Ordenar lista de mayor a menor.\n6. Almacenar la tabla ordenada.\n7. Salir del menu."))
    