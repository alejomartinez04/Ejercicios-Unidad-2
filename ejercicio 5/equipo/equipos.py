class equipo:
    __id:int
    __nom:str
    __golesf:int
    __golesc:int
    __difgoles:int
    __puntos:int
    def __init__(self, xiden, xnom, xgolesf, xgolesc, xdigfoles, xptos):
        self.__id=xiden
        self.__nom=xnom
        self.__golesf=xgolesf
        self.__golesc=xgolesc
        self.__difgoles=xdigfoles
        self.__puntos=xptos
    def getid(self):
        return self.__id
    def getnom(self):
        return self.__nom
    def getgolesf(self):
        return self.__golesf
    def getgolesc(self):
        return self.__golesc
    def getdifgoles(self):
        return self.__difgoles
    def getpuntos(self):
        return self.__puntos