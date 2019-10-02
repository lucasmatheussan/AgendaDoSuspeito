
class DadosSmartphone():
    def __init__(self, nome, numero, contatos,chamadas):
        self.__nome = nome
        self.__numero = numero
        self.__contatos = contatos
        self.__chamadas = chamadas

    @property
    def getNome(self):
        return self.__nome
    @getNome.setter
    def setNome (self,nome):
        self.__nome = nome
    @property
    def getNumero(self):
        return self.__numero
    @getNumero.setter
    def setNumero(self,numero):
        self.__numero = numero
    @property
    def getContatos(self):
        return self.__contatos
    @getContatos.setter
    def setContatos(self,contatos):
        self.__contatos = contatos
    @property
    def getChamadas(self):
        return self.__chamadas
    @getChamadas.setter
    def setChamadas(self,chamadas):
        self.__chamadas = chamadas
    def AcharContato(self, numero):
        if(numero in self.__contatos):
            return True
        else:
            return False
    def AcharChamadas(self, numero):
        if(numero in self.__chamadas):
            return True
        else:
            return False