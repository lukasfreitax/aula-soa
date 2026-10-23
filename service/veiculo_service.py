#Criação das validações e regras de negócio
from repository.veiculo_repository import VeiculoRepository

class VeiculoService:
    def __init__(self):
        self.__repository = VeiculoRepository()
        
    def cadastrar(self, veiculo):
        if veiculo.placa == "" or veiculo.modelo == "":
            raise ValueError("Placa e modelo são obrigatórios")
        if len(veiculo.placa)>8:
            raise ValueError("A placa deve conter até 8 dígitos")
        if len(veiculo.modelo)>50:
            raise ValueError("Modelo deve conter até 50 caracteres")
        self.__repository.cadastrar(veiculo)
        
    def listar(self):
        return self.__repository.listar()