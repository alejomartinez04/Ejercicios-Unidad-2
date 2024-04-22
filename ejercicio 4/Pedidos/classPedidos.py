class Pedido:
    __patenteas=str
    __iden=int
    __comidas=str
    __testimado=int
    __treal=int
    __precio=float
    def __init__(self,patente,id,comidas,testimado,precio):
        self.__patente=patente
        self.__iden=id
        self.__comidas=comidas
        self.__testimado=testimado
        self.__treal=0
        self.__precio=precio  