from Motos.classMotos import Moto
import csv
class gestormotos:
    __listamoto=list
    def __init__(self):
        self.__listamoto=[]
    def agregarmoto(self,unamoto):
        self.__listamoto.append(unamoto)
    def leerdatos(self):
        archivo=open('datosMoto.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera==True:
                bandera=False
            else:
                patente=fila[0]
                marca=fila[1]
                nya=fila[2]
                kilom=fila[3]
                unamoto=Moto(patente,marca,nya,kilom)
                self.agregarmoto(unamoto)
    def buscar(self,xpat):
        indice=0
        bandera=False
        while not bandera and indice < len(self.__listamoto):
            if self.__listamoto[indice].getpat()==xpat:
                bandera=True
            else:
                indice+=1
        return bandera