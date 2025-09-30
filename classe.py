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
    def __init__(self, tipoSSD_HDD, acapacidade_gb):
        self.__tipoSSD_HDD = tipoSSD_HDD
        self.__acapacidade_gb = acapacidade_gb

    def getTipo(self):
        return self.__tipoSSD_HDD
    
    def getAcapacidade_gb(self):
        return self.__acapacidade_gb
    
    def __str__(self):
        return f"Armazenamento: {self.__tipoSSD_HDD}, {self.__acapacidade_gb} GB"
    
class Computador:
    def __init__ (self, marca, modelo, modeloc, velocidade_ghz, capacidade_gb, tipo, tipoSSD_HDD, acapacidade_gb):
        self.__marca = marca
        self.__modeloc = modeloc
        self.__memoria_ram = MemoriaRAM(capacidade_gb, tipo)
        self.__processador = Processador(modelo, velocidade_ghz)
        self.__armazenamento = Armazenamento(tipoSSD_HDD, acapacidade_gb)

    def getMarca(self):
        return self.__marca

    def getModeloc(self):
        return self.__modeloc

    def getProcessador(self):
        return self.__processador

    def getMemoria_ram(self):
        return self.__memoria_ram

    def getArmazenamento(self):
        return self.__armazenamento
    
    def ligar(self):
        print(f"\n Ligando o computador {self.getMarca()} {self.getModeloc()}...")
        print(f" {self.getProcessador()}")
        print(f" {self.getMemoria_ram()}")
        print(f" {self.getArmazenamento()}")
        return self
    
    def __str__(self):
        return (f"Computador: {self.__marca} {self.__modeloc}\n"
                f"{self.__processador}\n"
                f"{self.__memoria_ram}\n"
                f"{self.__armazenamento}")

    def __del__(self):
        print(f"[DESMONTANDO] Computador {self.__marca} foi desmontado")