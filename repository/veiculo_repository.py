from database import Session
from model.veiculo import Veiculo

class VeiculoRepository:
    def __init__(self):
        self.__session = Session()
        
    def cadastrar(self, veiculo):
        self.__session.add(veiculo)
        self.__session.commit()
        self.__session.close()
        
    def listar(self):
        veiculos = self.__session.query(Veiculo).all()
        self.__session.close()
        return veiculos
    