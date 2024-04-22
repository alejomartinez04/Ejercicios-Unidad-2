from Motos.classMotos import Moto
from Motos.GestorMotos import gestormotos
from Pedidos.classPedidos import Pedido
from Pedidos.GestorPedidos import gestorpedido
if __name__=='__main__':
    gestorm=gestormotos
    gestorp=gestorpedido
    opcion=str(input("Ingrese numero de opcion:\n1. Leer datos de motos.\n2. Leer datos de pedidos.\n3. Agregar pedido.\n4. Tiempo real de entrega.\n5. Tiempo promedio de un repartidor.\n6. Generar lista por moto"))
    if opcion=='1':
        gestorm.leerdatos()
    elif opcion=='2':
        gestorp.leerdatos()