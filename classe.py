class Processador:
    def __init__ (self, modelo:str, velocidade_ghz:float):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz
    
    def getModelo(self):
        return self.__modelo
    
    def getVelocidade_ghz(self):
        return self.__velocidade_ghz

class Computador:
    def __init__ (self, marca:str, modelo:str):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria_ram = MemoriaRAM()
        self.__processador = Processador()
        self.__armazenamento = Armazenamento()
