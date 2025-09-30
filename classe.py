class Processador:
    def __init__ (self, modelo:str, velocidade_ghz:float):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz
    
    def getModelo(self):
        return self.__modelo
    
    def getVelocidade_ghz(self):
        return self.__velocidade_ghz
    
class MemoriaRAM:
    def __init__(self, capacidade_gb:float, tipo:str):
        self.__capacidade_gb = capacidade_gb
        self.__tipo = tipo

    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
    def getTipo(self):
        return self.__tipo

class Armazenamento:
    def __init__(self, tipo:str, capacidade_gb):
        self.__tipo = tipo
        self.__capacidade_gb = capacidade_gb

    def getTipo(self):
        return self.__tipo
    
    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
class Computador:
    def __init__ (self, marca:str, modelo:str):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria_ram = MemoriaRAM()
        self.__processador = Processador()
        self.__armazenamento = Armazenamento()
