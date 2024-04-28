import datetime
class fecha:
    __fe:datetime
    __idlocal:int
    __idvis:int
    __cantgl:int
    __cantgv:int
    def __init__(self, xfe, xidl, xidv, cgl, cgv):
        self.__fe=xfe
        self.__idlocal=xidl
        self.__idvis=xidv
        self.__cantgl=cgl
        self.__cantgv=cgv
    def getfecha(self):
        return self.__fe
    def getidlocal(self):
        return self.__idlocal
    def getidvisitante(self):
        return self.__idvis
    def getcantgl(self):
        return self.__cantgl
    def getcantgv(self):
        return self.__cantgv