class Processador:
    def __init__ (self, modelo:str, velocidade_ghz:float):
        self.__modelo = modelo
        self.__velocidade_ghz = velocidade_ghz
    
    def getModelo(self):
        return self.__modelo
    
    def getVelocidade_ghz(self):
        return self.__velocidade_ghz
    
    def __str__(self):
        return f"Processador: {self.__modelo}, {self.__velocidade_ghz} GHz"
    
class MemoriaRAM:
    def __init__(self, capacidade_gb:float, tipo:str):
        self.__capacidade_gb = capacidade_gb
        self.__tipo = tipo

    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"Memória RAM: {self.__capacidade_gb} GB, Tipo: {self.__tipo}"

class Armazenamento:
    def __init__(self, tipo:str, capacidade_gb):
        self.__tipo = tipo
        self.__capacidade_gb = capacidade_gb

    def getTipo(self):
        return self.__tipo
    
    def getCapacidade_gb(self):
        return self.__capacidade_gb
    
    def __str__(self):
        return f"Armazenamento: {self.__tipo}, {self.__capacidade_gb} GB"
    
class Computador:
    def __init__ (self, marca:str, modelo:str):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria_ram = MemoriaRAM()
        self.__processador = Processador()
        self.__armazenamento = Armazenamento()

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getProcessador(self):
        return self.__processador

    def getMemoria_ram(self):
        return self.__memoria_ram

    def getArmazenamento(self):
        return self.__armazenamento
