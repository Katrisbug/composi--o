
class Computador:
    def __init__ (self, marca:str, modelo:str):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria_ram = MemoriaRAM()
        self.__processador = Processador()
        self.__armazenamento = Armazenamento()
