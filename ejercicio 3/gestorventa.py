class GestorVentas:
    __ventas = [5]
    __cantfarmacias = int
    __cantdias = 7
    def __init__(self):
        cantfarmacias = 5
        cantdias = 7
        for i in range (cantfarmacias):
            self.__ventas.append([0]*self.__cantdias)
    def acumular (self, nd, ns, importe):
        self.__ventas[ns-1][nd-1]+=importe
    def totalxd(self, ns, importe):
        importe = 0
        ns = input("Ingrese sucursal: ")
        for i in range (self.__cantdias):
            importe+=self.__ventas[ns-1][i]
        return importe
    def masfacturo(self, nd, max):
        max = 0
        nd = input("Ingrese día de la semana: ")
        for i in range (self.__cantfarmacias):
            if max > (self.__ventas[i][nd-1]):
                max = i+1
        return max
    def menosfacturo(self, min, acum):
        min=99999999999
        for i in range (self.__cantfarmacias):
            acum = 0
            for j in range (self.__cantdias):
                acum+=self.__ventas[i][j]
            if acum < min:
                min = acum
            