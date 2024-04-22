class Moto:
    __patente=str
    __marca=str
    __nya=str
    __kilometraje=int
    def __init__(self,pat,marca,nya,kilo):
        self.__patente=pat
        self.__marca=marca
        self.__nya=nya
        self.__kilometraje=kilo
    def getpat(self):
        return self.__patente
    def getmarca(self):
        return self.__marca
    def getnya(self):
        return self.__nya
    def getkilometraje(self):
        return self.__kilometraje