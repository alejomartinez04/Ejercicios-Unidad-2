from classPedidos import Pedido
import csv
class gestorpedido:
    __listapedido=list
    def __init__(self):
        self.__listapedido=[]
    def agregarpedido(self,unpedido):
        self.__listapedido.append(unpedido)
    def leerdatos(self):
        archivo=open('datosPedido.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera==True:
                bandera=False
            else:
                patenteasignada=fila[0]
                id=fila[1]
                comidas=fila[2]
                testimado=fila[3]
                treal=fila[4]
                importe=fila[5]
                unpedido=Pedido(patenteasignada,id,comidas,testimado,treal,importe)
                self.agregarpedido(unpedido)