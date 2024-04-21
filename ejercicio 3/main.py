from gestorventa import GestorVentas
if __name__=='__main__':
    confirmar=str(input("¿Acceder a una funcionalidad? si/no: "))
    gestor=GestorVentas()
    while (confirmar=='si'):
        opcion=str(input("'1' - Ingresar el importe de un dia de una sucursal.\n'2' - Obtener factura de una sucursal.\n'3' - Obtener la sucursal que más facturó un día.\n'4' - Obtener la sucursal que menos facturó en toda la semana.\n'5' - Obtener el total facturado de todas las sucursales.\n'6' - Salir del menú.\n"))
        if opcion=='1':
            xns=int(input("Ingresar una sucursal (de 1 a 5): "))
            xnd=int(input("Ingresar un día de la semana (de 1 a 7): "))
            ximp=float(input("Ingresar importe: "))
            gestor.acumular(xns,xnd,ximp)
        elif opcion=='2':
            xns=int(input("Ingresar una sucursal (de 1 a 5): "))
            print("El total de esa sucursal es: {}".format(gestor.total(xns)))
        elif opcion=='3':
            xnd=int(input("Ingresar un día de la semana (de 1 a 7): "))
            print("La sucursal que más facturó ese día fue la {}".format(gestor.masfacturo(xnd)))
        elif opcion=='4':
            print("La sucursal que menos facturó en la semana fue la {}".format(gestor.menosfacturo()))
        elif opcion=='5':
            print("El total facturado por todas las sucursales durante la semana fue: {}".format(gestor.totalfacturado()))
        elif opcion=='6':
            confirmar=='no'