class GestorVentas:
    __ventas = [5]
    __cantfarmacias = 5
    __cantdias = 7
    def __init__(self):
        for i in range (self.__cantfarmacias):
            self.__ventas.append([0]*self.__cantdias)
        pass
    def acumular (self, ns, nd, importe):
        self.__ventas[ns-1][nd-1] += importe
    def total(self, ns):
        importe = 0
        for i in range (self.__cantdias):
            importe+=self.__ventas[ns-1][i]
        return importe
    def masfacturo(self, nd):
        max = 0
        aux=0
        for i in range (self.__cantfarmacias):
            if max < (self.__ventas[i][nd-1]):
                aux = i+1
                max=self.__ventas[i][nd-1]
        return aux
    def menosfacturo(self):
        min=99999999999
        aux=0
        for i in range (self.__cantfarmacias):
            acum = 0
            for j in range (self.__cantdias):
                acum+=self.__ventas[i][j]
            if acum < min:
                min = acum
                aux=i+1
        return aux
    def totalfacturado(self):
        acum=0
        for i in range (self.__cantfarmacias):
            for j in range (self.__cantdias):
                acum+=self.__ventas[i][j]
        return acum