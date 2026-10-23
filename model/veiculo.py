from sqlalchemy import Column, Integer, String
from database import Base

class Veiculo(Base):
    __tablename__ = "veiculo"
    id = Column(Integer, autoincrement=True, primary_key=True)
    placa = Column(String(8), nullable=False)
    modelo = Column(String(50), nullable=False)
    
#criacao do construtor
    def __init__(self, placa:str, modelo:str):
        self.placa = placa
        self.modelo = modelo
        
    def to_dict(self):
        return{
            "id":self.id,
            "placa":self.placa,
            "modelo":self.modelo
        }
        
            
    
